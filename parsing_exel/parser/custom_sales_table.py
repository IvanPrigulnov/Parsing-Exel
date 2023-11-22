from tablib import Dataset


def sales_row_coll_converter(dataset: Dataset,
                             number_of_columns: int = 6
                             ) -> Dataset:
    arr_data = dataset.dict
    new_arr_data = []
    months = {
        'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
        'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
    }
    years = {'2023', '2024'}
    row = 0
    while row < len(arr_data):
        inter_dict = {}
        for heading in arr_data[row]:
            inter_dict[heading] = arr_data[row][heading]
            for year in years:
                for month in months:
                    if month in heading and year in heading:
                        inter_dict['Год'] = year
                        inter_dict['Месяц'] = month
                        inter_dict['Статус'] = inter_dict.pop(heading)

            if len(inter_dict) == number_of_columns:
                new_arr_data.append(inter_dict.copy())
        inter_dict.clear()
        row += 1
    new_dataset = Dataset()
    new_dataset.dict = new_arr_data
    return new_dataset
