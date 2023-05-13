import timeit


def one1():
    return list(range(0, 13 ** 7, 2))


print(timeit.timeit(one1, number=3))

# ------------------------------------------------


def one2():
    return [x for x in range(0, 13 ** 7, 2)]


print(timeit.timeit(one2, number=3))

# ------------------------------------------------


def one3():
    return [x for x in range(13 ** 7) if not x & 1]


print(timeit.timeit(one3, number=3))

# ------------------------------------------------


def one():
    return [x for x in range(13 ** 7) if not x % 2]


print(timeit.timeit(one, number=3))

# ------------------------------------------------


def one4():
    return list(filter(lambda x: not x & 1, range(13 ** 7)))


print(timeit.timeit(one4, number=3))
