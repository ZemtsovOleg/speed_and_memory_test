import timeit


def sum_example() -> int:
    return sum(range(1000000))


print(timeit.timeit(sum_example, number=5))

# ------------------------------------------------


def sum_example1() -> int:
    return sum(num for num in range(1000000))


print(timeit.timeit(sum_example1, number=5))
