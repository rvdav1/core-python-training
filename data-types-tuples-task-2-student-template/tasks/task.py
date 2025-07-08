from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    # TODO: Add your code here
    iterations = len(lst) - 1
    pairs = []
    if iterations < 1:
        return pairs
    for i in range(iterations):
        pairs.append((lst[i], lst[i+1]))
    return pairs