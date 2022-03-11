import csv
import pandas as pd
from io import BytesIO, IOBase, StringIO
from operator import attrgetter
from typing import Callable, Iterable, OrderedDict, Union

from logger import logged

FieldsType = OrderedDict[str, Union[str, Callable]]


def get_row(data, fields: FieldsType):
    row = []
    for field_getter in fields.values():
        if isinstance(field_getter, str):
            row.append(attrgetter(field_getter)(data))
        else:
            row.append(field_getter(data))
    return row


@logged
def handle_xlsx(file: StringIO) -> BytesIO:
    file.seek(0)
    df = pd.read_csv(file)
    file = BytesIO()
    with pd.ExcelWriter(file, engine="xlsxwriter") as writer:
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

    if as_xlsx:
        return handle_xlsx(file)

    return file
