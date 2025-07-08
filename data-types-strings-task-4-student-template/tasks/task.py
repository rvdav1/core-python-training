import re

def check_str(s: str):
    """
    Add your code here
    """
    alphanumeric_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    length = len(alphanumeric_s)
    for i, c in enumerate(alphanumeric_s):
        if c != alphanumeric_s[length - i - 1]:
            return False
    return True