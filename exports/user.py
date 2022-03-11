from collections import OrderedDict

from data import Address, User, session

from exports.common.generic_export import generic_export
from exports.common.utils import get_relationship_fields
from logger import logged


@logged
def get_data():
    return session.query(User).all()


@logged
def export_users():
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
                        user.addresses,
                    )
                ),
            ),
            ("Position", "position.name"),
        ]
    )
    data = get_data()
    print(f"retrieved {len(data)} users")
    return generic_export(fields, data, as_xlsx=True)
