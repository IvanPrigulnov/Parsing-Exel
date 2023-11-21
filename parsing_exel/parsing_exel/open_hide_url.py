import tablib
from import_export.formats import base_formats


class XLSXWithHideURL(base_formats.XLSX):
    def create_dataset(self, in_stream):
        from io import BytesIO
        import openpyxl
        # в оригинале read_only=True
        xlsx_book = openpyxl.load_workbook(BytesIO(in_stream), read_only=False,
                                           data_only=True)
        dataset = tablib.Dataset()
        sheet = xlsx_book.active
        rows = sheet.rows
        dataset.headers = [cell.value for cell in next(rows)]

        for row in rows:
            # в оригинале row_values = [cell.value for cell in row]
            # изменено для чтения URL скрытого за текстом
            row_values = [cell.value if cell.hyperlink is None else cell.hyperlink.target for cell in row]
            dataset.append(row_values)
        return dataset
