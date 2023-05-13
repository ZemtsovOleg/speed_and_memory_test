import timeit
import random


lst = [9, 3, '7', '3', '5', '0', 9, 3, 2, 1, '9', 6, 7, '3', 6, 6, 0, '5', 8, 5, '6', 2, '0', '1', '5', '8', 8, 9, 9, 2, '3', 8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7, 9, 3, '7', '3', '5', '0', 9, 3, 2, 1, '9', 6, 7, '3', 6, 6, 0, '5', 8, 5, '6', 2, '0', '1', '5', '8', 8, 9, 9, 2, '3', 8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7,
       9, 3, '7', '3', '5', '0', 9, 3, 2, 1, '9', 6, 7, '3', 6, 6, 0, '5', 8, 5, '6', 2, '0', '1', '5', '8', 8, 9, 9, 2, '3', 8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7, 9, 3, '7', '3', '5', '0', 9, 3, 2, 1, '9', 6, 7, '3', 6, 6, 0, '5', 8, 5, '6', 2, '0', '1', '5', '8', 8, 9, 9, 2, '3', 8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7, 9, 3, '7', '3', '5', '0', 9, 3, 2, 1, '9', 6, 7, '3', 6, 6, 0, '5', 8, 5, '6', 2, '0', '1', '5', '8', 8, 9, 9, 2, '3', 8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7, 9, 3, '7', '3', '5', '0', 9, 3, 2, 1, '9', 6, 7, '3', 6, 6, 0, '5', 8, 5, '6', 2, '0', '1', '5', '8', 8, 9, 9, 2, '3', 8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7,
       9, 3, '7', '3', '5', '0', 9, 3, 2, 1, '9', 6, 7, '3', 6, 6, 0, '5', 8, 5, '6', 2, '0', '1', '5', '8', 8, 9, 9, 2, '3', 8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7, 9, 3, '7', '3', '5', '0', 9, 3, 2, 1, '9', 6, 7, '3', 6, 6, 0, '5', 8, 5, '6', 2, '0', '1', '5', '8', 8, 9, 9, 2, '3', 8, 0, 0, 8, 5, 2, 3, 7, 8, 6, 7] * 9000


# def sum_mix(arr) -> int:
#     return sum(map(int, arr))


# print(timeit.timeit(lambda: sum_mix(lst), number=3))


# def sum_mix1(arr) -> int:
#     return sum(int(i) for i in arr)


# print(timeit.timeit(lambda: sum_mix1(lst), number=3))

# ------------------------------------------------


def count_strings(arr: list) -> int:
    count = 0
    for i in arr:
        if isinstance(i, str):
            count += 1
    return count


print(timeit.timeit(lambda: count_strings(lst), number=30))

# ------------------------------------------------


def count_strings1(arr: list) -> int:
    return sum(map(lambda x: isinstance(x, str), arr))


print(timeit.timeit(lambda: count_strings1(lst), number=30))

# ------------------------------------------------


def count_strings2(arr: list) -> int:
    return sum(1 for v in arr if isinstance(v, str))


print(timeit.timeit(lambda: count_strings2(lst), number=30))

# ------------------------------------------------


def count_strings3(arr: list) -> int:
    return sum(isinstance(x, str) for x in arr)


print(timeit.timeit(lambda: count_strings3(lst), number=30))
