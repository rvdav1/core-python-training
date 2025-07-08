from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    """
    Add your code here or call it from here   
    """
    d = {}
    for i in range(1, num + 1):
        d[i] = i ** 2
    return d