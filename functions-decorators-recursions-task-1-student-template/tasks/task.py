from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    """
    Add your code here or call it from here   
    """
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple, set)):
            total += seq_sum(item)
        elif isinstance(item, dict):
            total += seq_sum(item.values())
        elif isinstance(item, (int, float)):
            total += item
    return total
