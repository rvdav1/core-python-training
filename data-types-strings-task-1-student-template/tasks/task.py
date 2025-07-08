def get_fractions(a_b: str, c_b: str) -> str:
    """
    Add your code here  
    """
    sum_result = get_sum_result(a_b, c_b)
    result = f'{a_b} + {c_b} = {sum_result}'
    return result

def get_sum_result(a_b: str, c_b: str) -> str:
    a, b = get_number_parts(a_b)
    c, d = get_number_parts(c_b)
    fraction = a + c
    if b == d:
        denominator = b
    else:
        denominator = (b + d) // 2
    return f'{fraction}/{denominator}'

def get_number_parts(x_y: str) -> tuple[int, int]:
    division_index = x_y.find('/')
    if division_index == -1:
        return int(x_y), 1
    x = int(x_y[:division_index])
    y = int(x_y[division_index + 1:])
    return x, y