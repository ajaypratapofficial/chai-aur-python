# Create a decorator that will print out how long a function took to run

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper


# example_function will be passed as argument to timer first
@timer
def example_function(n):
    time.sleep(n)

example_function(2)