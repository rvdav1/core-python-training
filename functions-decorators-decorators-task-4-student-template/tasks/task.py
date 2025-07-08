from functools import wraps

def decorator_apply(lambda_func):
    '''
    Add your implementation here
    '''
    def decorator(inner_func):
        @wraps(inner_func)
        def wrapper(*args, **kwargs):
            result = inner_func(*args, **kwargs)
            return lambda_func(result)
        return wrapper
    return decorator


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num
