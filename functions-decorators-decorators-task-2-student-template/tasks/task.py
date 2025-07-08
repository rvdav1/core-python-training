import time

def log(fn):
    """
    Add your code here or call it from here   
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time 
        log_entry = create_log_entry(fn, execution_time, *args, **kwargs)
        with open("log.txt", "a") as log_file:
            log_file.write(log_entry)
        return result
    return wrapper

def create_log_entry(fn, execution_time, *args, **kwargs):
    arg_str = ", ".join(f"{key}={value}" for key, value in zip(fn.__code__.co_varnames, args))
    kwarg_str = ", ".join(f"{key}={value}" for key, value in kwargs.items())
    return f"{fn.__name__}; args: {arg_str}; kwargs: {kwarg_str}; execution time: {execution_time:.2f} sec.\n"