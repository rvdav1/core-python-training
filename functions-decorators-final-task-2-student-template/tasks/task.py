from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    """
    Add your code here or call it from here   
    """
    last_valid_index = 0
    result = []
    length = len(s)
    for i in indexes:
        if is_index_valid(i, last_valid_index, length):
            result.append(s[last_valid_index:i])
            last_valid_index = i
    if last_valid_index < length:
        result.append(s[last_valid_index:])
    return result

def is_index_valid(index: int, floor: int, ceil: int) -> bool:
    return index > floor and index <= ceil