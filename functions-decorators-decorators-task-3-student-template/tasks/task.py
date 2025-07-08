
def validate(fn):
    '''
    Add corresponded arguments and implementation here. 
    '''
    def wrapper(*args, **kwargs):
          error_msg = "Function call is not valid!"
          for arg in args:
              if not is_valid(arg):
                  return error_msg
          for arg in kwargs:
              if not is_valid(arg):
                  return error_msg
          return fn(*args, **kwargs)
    return wrapper
  
def is_valid(x: int) -> bool:
      return x >= 0 and x <= 256

@validate
def set_pixel(x: int, y: int, z: int) -> str:
  return "Pixel created!"