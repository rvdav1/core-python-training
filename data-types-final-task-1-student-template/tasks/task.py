from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    """
    Add your code here or call it from here   
    """
    result = set()
    for d in lst:
        result.update(d.values())
    return result
