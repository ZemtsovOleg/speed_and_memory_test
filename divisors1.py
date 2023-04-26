# Программа считает количество делителей
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
def divisors(integer):
    i, result = 1, 0
    while i * i <= integer:
        if not integer % i:
            result += 1
            if i != integer // i:
                result += 1
        i += 1
    return result

divisors(99999999)

#------------------------------------------------

@decorator_time
def divisors2(n):
    divs = 0
    for x in range(1, int(n ** 0.5) +1):
        if n % x == 0:
            divs += 2
    return divs - (x * x == n)

divisors2(99999999)

#------------------------------------------------

# медленный 
# @decorator_time
# def divisors1(integer):
#     i=0
#     for n in range(2, (integer // 2) + 1):
#         if not integer % n:
#             i+=1
#     return i

# divisors1(99999)