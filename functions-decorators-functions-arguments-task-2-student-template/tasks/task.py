def union(*args) -> set:
    return create_union(*args)

def intersect(*args) -> set:
    union_res = create_union(*args)
    result = set()
    for elem in union_res:
        if is_intersect(elem, *args):
            result.add(elem)
    return result

def create_union(*args) -> set:
    result = set()
    for arg in args:
        for elem in arg:
            result.add(elem)
    return result

def is_intersect(elem, *args) -> bool:
    for arg in args:
        if elem not in arg:
            return False
    return True