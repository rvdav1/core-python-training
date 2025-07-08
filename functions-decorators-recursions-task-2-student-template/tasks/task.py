from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    """
    Add your code here or call it from here   
    """
    result = []
    for item in sequence:
        if isinstance(item, (list, tuple, set)):
            result.extend(linear_seq(item))
        else:
            result.append(item)
    return result

