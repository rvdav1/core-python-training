from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    # TODO: Add your code here
    return tuple(int(digit) for digit in str(num))