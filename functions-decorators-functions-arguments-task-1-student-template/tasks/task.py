from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters.

    :param data: List of dictionaries with columns and values.
    :param selector: Result of `select` function call.
    :param filters: Any number of results of `field_filter` function calls.
    :return: Filtered data.
    """
    for filter_func in filters:
        data = filter_func(data)
    data = selector(data)
    return list(data)

def select(*columns: str) -> ModifierFunc:
    """
    Return function that selects only specific columns from dataset
    
    :param columns: Names of columns to select.
    :return: A function that modifies the dataset to include only the specified columns.
    """
    def selector(data: DataType) -> DataType:
        return [{col: record[col] for col in columns if col in record} for record in data]
    return selector

def field_filter(column: str, *values: Any) -> ModifierFunc:
    """
    Return a function that filters a specific column to be one of `values`.

    :param column: Name of the column to filter.
    :param values: Allowed values for the column.
    :return: A function that filters the dataset based on the column and values.
    """
    def filter_func(data: DataType) -> DataType:
        return [record for record in data if record.get(column) in values]
    return filter_func

def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()

