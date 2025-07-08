from typing import Dict

def combine_dicts(*args:Dict[str, int]) -> Dict[str, int]:
    result = {}
    for arg in args:
        for key, value in arg.items():
            if key in result:
                result[key] += value
            else:  
                result[key] = value
    return result
