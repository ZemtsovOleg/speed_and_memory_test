import datetime

def decorator_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        print(datetime.datetime.now() - start)
        return result

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

#------------------------------------------------

@decorator_time
def sum_example1():
    return sum(range(10000000))

sum_example1()

#------------------------------------------------

@decorator_time
def sum_example2():
    return sum(num for num in range(10000000))

sum_example2()

#------------------------------------------------

@decorator_time
def cycle_example():
    result = 0
    for num in range(10000000):
        result += num
    return result

cycle_example()