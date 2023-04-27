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

#-----------------------------------------------------------

@decorator_time
def divisors(integer):
    i = 2
    dividers = []
    while i * i <= integer:
        if not integer % i:
            dividers.append(i)
            if i != integer // i:
                dividers.append(integer // i)
        i += 1
    return sorted(dividers) or f'{integer} is prime'

print(divisors(999))

#-----------------------------------------------------------

# медленный 
@decorator_time
def divisors1(integer):
    return [n for n in range(2, (integer // 2) + 1) if not integer % n] or f'{integer} is prime'

divisors1(999)