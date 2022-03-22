from collections import OrderedDict, defaultdict
import random

from data import Address, User, UserPosition, session

from exports.common.generic_export import generic_export
from exports.common.utils import get_relationship_fields
from logger import logged

from sqlalchemy.engine import CursorResult
from sqlalchemy.sql import select


@logged
def get_data() -> CursorResult:
    stmt = select(User)
    return session.get_bind().execute(stmt).fetchall()

@logged
def get_addresses_per_user_id():
    addresses = session.get_bind().execute(select(Address)).fetchall()
    addresses_per_user_id = defaultdict(list)
    for address in addresses:
        addresses_per_user_id[address.user_id].append(address)
    return addresses_per_user_id


@logged
def export_users():
    data = get_data()
    addresses_per_user_id = get_addresses_per_user_id()
    fields = OrderedDict(
        [
            ("ID", "id"),
            ("Nom", "name"),
            ("Age", "age"),
            *get_relationship_fields(
                Address.country,
                lambda country: country.country,
                lambda country, user: ",".join(
                    map(
                        lambda address: address.name
                        if address.country == country.country
                        else "",
                        addresses_per_user_id[user.id],
                    )
                ),
            ),
            ("Position", "name_1"),
            ("Workload", lambda user: user.age * random.randint(1, 10)),
            ("foo", lambda user: user.age * random.randint(1, 10)),
            ("bar", lambda user: user.age * random.randint(1, 10)),
            ("baz", lambda user: user.age * random.randint(1, 10)),
            ("lol", lambda user: user.age * random.randint(1, 10)),
            ("oui", lambda user: user.age * random.randint(1, 10)),
            ("non", lambda user: user.age * random.randint(1, 10)),
        ]
    )
    return generic_export(fields, data, as_xlsx=False)
