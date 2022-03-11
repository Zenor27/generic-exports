from typing import Callable
from data import session


def get_relationship_fields(model_to_query, field_name_getter: Callable, field_value_getter: Callable):
    relationships = session.query(model_to_query).distinct().all()
    fields = []
    for relationship in relationships:
        fields.append(
            (
                field_name_getter(relationship),
                lambda data: field_value_getter(relationship, data)
            )
        )
    return fields


