from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    # TODO: Add your code here
    char_count = {}
    for char in s:
        lower_char = char.lower()
        char_count[lower_char] = char_count.get(lower_char, 0) + 1
    return char_count