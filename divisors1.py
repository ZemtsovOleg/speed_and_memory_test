import timeit

''' Программа считает количество делителей '''


def divisors(n: int) -> int:
    divs = 0
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            divs += 2
    return divs - (x * x == n)


print(timeit.timeit(lambda: divisors(2999999), number=12))

# ------------------------------------------------


def divisors1(integer: int) -> int:
    i, result = 1, 0
    while i * i <= integer:
        if not integer % i:
            result += 1
            if i != integer // i:
                result += 1
        i += 1
    return result


print(timeit.timeit(lambda: divisors1(2999999), number=12))

# ------------------------------------------------
# медленный


# def divisors2(integer: int) -> int:
#     i = 0
#     for n in range(2, (integer // 2) + 1):
#         if not integer % n:
#             i += 1
#     return i


# print(timeit.timeit(lambda: divisors2(2999999), number=12))
