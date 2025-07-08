def replacer(s: str) -> str:
    """
    Add your code here
    """
    result = ''
    for c in s:
        if c == "'":
            result += '"'
        elif c == '"':
            result += "'"
        else:
            result += c
    return result