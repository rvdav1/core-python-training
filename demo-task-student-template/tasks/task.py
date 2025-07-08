from typing import Tuple, Union
from math import sqrt

def solution(a, b, c) -> Union[Tuple[float, float], Tuple[float], None]:

    result = None
    # Add your code here or call it from here
    result = solve_with_format(a, b, c)
    return result 

def solve_with_format(a, b, c):
    result = solve(a, b, c)
    if result:
        result = tuple(int(x) if isinstance(x, float) and x.is_integer() else x for x in result)
    return result

def solve(a, b, c):
    if a == 0:
        if b == 0:
            return None if c != 0 else float('inf')
        return (-c / b,)  # Single root for linear equation

    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # No real roots

    root1 = (-b + sqrt(discriminant)) / (2 * a)
    root2 = (-b - sqrt(discriminant)) / (2 * a)

    if root1 == root2:
        return (root1,)  # Return single root if both roots are the same
    return tuple(sorted((root1, root2)))  # Return roots in ascending order