import timeit

# $ python -m timeit -s'xs=range(10)' 'map(hex, xs)'
# 100000 loops, best of 3: 4.86 usec per loop

# $ python -m timeit -s'xs=range(10)' '[hex(x) for x in xs]'
# 100000 loops, best of 3: 5.58 usec per loop
# Пример того, как сравнение производительности становится полностью обратным, когда карте нужна лямбда:

# $ python -m timeit -s'xs=range(10)' 'map(lambda x: x+2, xs)'
# 100000 loops, best of 3: 4.24 usec per loop

# $ python -m timeit -s'xs=range(10)' '[x+2 for x in xs]'
# 100000 loops, best of 3: 2.32 usec per loop

numbers = list(range(1, 1000000))


def two(lst: list) -> list:
    return list(filter(lambda x: not x & 1, lst))


print(timeit.timeit(lambda: two(numbers), number=10))

# ------------------------------------------------


def two1(lst: list) -> list:
    return [x for x in lst if not x & 1]


print(timeit.timeit(lambda: two1(numbers), number=10))
