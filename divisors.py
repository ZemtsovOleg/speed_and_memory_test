''' Нахождение делителей числа '''


import timeit


def divisors(integer: int) -> list:
    i = 2
    dividers = []
    while i * i <= integer:
        if not integer % i:
            dividers.append(i)
            if i != integer // i:
                dividers.append(integer // i)
        i += 1
    return sorted(dividers) or f'{integer} is prime'


print(timeit.timeit(lambda: divisors(2999999), number=12))


def divisors1(integer: int) -> list:
    return [n for n in range(2, (integer // 2) + 1) if not integer % n] or f'{integer} is prime'


print(timeit.timeit(lambda: divisors1(2999999), number=12))
