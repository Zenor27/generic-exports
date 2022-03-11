from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import relationship, Session, backref
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.pool import QueuePool

from logger import logged

BaseModel = declarative_base()


class User(BaseModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


class UserPosition(BaseModel):
    __tablename__ = "user_position"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(
        "User", backref=backref("position", uselist=False, lazy="joined")
    )


class Address(BaseModel):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", backref=backref("addresses", lazy="joined"))


engine: Engine = create_engine(
    "sqlite:///data.db",
    poolclass=QueuePool,
    connect_args={"check_same_thread": False},
)
User.metadata.create_all(engine)
Address.metadata.create_all(engine)
session: Session = sessionmaker(bind=engine)()


@logged
def generate_users(COUNT: int = 10):
    users = []
    for i in range(COUNT):
        position = UserPosition(name=f"Position {i}")
        user = User(name=f"User {i}", age=i, position=position)
        users.append(user)
    session.add_all(users)
    session.commit()


@logged
def generate_addresses():
    addresses = []
    for user in session.query(User).all():
        for i in range(10):
            address = Address(
                name=f"Address {i}",
                user_id=user.id,
                country="FR" if i % 2 == 0 else "US",
            )
            addresses.append(address)
    session.add_all(addresses)
    session.commit()
