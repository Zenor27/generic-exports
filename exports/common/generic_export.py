import csv
import pandas as pd
from io import BytesIO, IOBase, StringIO
from operator import attrgetter
from typing import Callable, Iterable, OrderedDict, Union

from logger import logged

FieldsType = OrderedDict[str, Union[str, Callable]]

NA = "N/A"


def get_row(data, fields: FieldsType):
    row = []
    row_append = row.append
    for field_getter in fields.values():
        if isinstance(field_getter, str):
            try:
                field_value = attrgetter(field_getter)(data)
            except AttributeError:
                print(f"Attribute {field_getter} not found")
                field_value = None
        else:
            field_value = field_getter(data)
        row_append(field_value or NA)
    return row


@logged
def handle_xlsx(file: StringIO) -> BytesIO:
    df = pd.read_csv(file)
    file = BytesIO()
    with pd.ExcelWriter(
        file,
        engine="xlsxwriter",
        options={"strings_to_url": False},
    ) as writer:
        df.to_excel(writer, index=False, encoding="utf-8")
    file.seek(0)
    return file


@logged
def generic_export(
    fields: FieldsType, datas: Iterable, file: BytesIO = None, as_xlsx=False
) -> IOBase:
    file = file or StringIO()
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    headers = fields.keys()
    writer.writerow(headers)

    rows = []
    append_row = rows.append
    [append_row(get_row(data, fields)) for data in datas]
    writer.writerows(rows)
    file.seek(0)

    if as_xlsx:
        return handle_xlsx(file)

    return file
