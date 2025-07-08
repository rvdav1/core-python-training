from typing import List

def split(data: str, sep=None, maxsplit=-1):
    """
    Add your code here or call it from here   
    """
    if sep is None:
        return split_whitespace(data, maxsplit)

    return split_non_whitespace(data, sep, maxsplit)


def split_whitespace(data: str, maxsplit):
    if maxsplit == 0:
        return [data.lstrip()]
    result = []
    word = ""
    count = 0
    for char in data:
        if char.isspace():
            if word:
                result.append(word)
                word = ""
                count += 1
                if maxsplit != -1 and count >= maxsplit:
                    print(f"curRes {result} and word {word}")
                    break
        else:
            word += char
    if word or maxsplit == 0:
        result.append(word)
    if maxsplit != -1 and count >= maxsplit:
        remaining = data[data.index(result[-1]) + len(result[-1]):].lstrip()
        result.append(remaining)
    return result


def split_non_whitespace(data: str, sep, maxsplit):
    if maxsplit == 0:
        return [data.lstrip(sep)]
    result = []
    word = ""
    count = 0
    sep_len = len(sep)
    i = 0
    while i < len(data):
        if data[i:i + sep_len] == sep:
            result.append(word)
            word = ""
            count += 1
            i += sep_len
            if maxsplit != -1 and count >= maxsplit:
                break
        else:
            word += data[i]
            i += 1
    if word or maxsplit == 0:  # Ensure the last word or handle maxsplit=0
        result.append(word)
    if maxsplit != -1 and count >= maxsplit:
        remaining = data[i:]
        result.append(remaining)
    else:
        if data.endswith(sep):
            result.append("")
    return result

if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']