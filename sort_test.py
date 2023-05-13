import random
import timeit


lst = [random.randint(-10000, 10000) for _ in range(5000)]
lst1 = lst[:]
lst2 = lst[:]
lst3 = lst[:]

# ------------------------------------------------

# def sort_my(lst):
#     for index in range(len(lst) - 1):
#         count = index + 1
#         while count < len(lst):
#             if lst[index] > lst[count]:
#                 lst[index], lst[count] = lst[count], lst[index]
#             else:
#                 count += 1
#     return lst

# print(timeit.timeit(lambda: sort_my(lst), number=1))

# ------------------------------------------------


def bubble_sort(lst):
    for x in range(l := len(lst)):
        done = True
        for i in range(l - 1 - x):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                done = False
        if done:
            break
    return lst


print(timeit.timeit(lambda: bubble_sort(lst1), number=1))

# ------------------------------------------------


def my_insertion_sort(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            for y in range(len(lst[0:i])):
                if lst[i] < lst[y]:
                    lst[i], lst[y] = lst[y], lst[i]
    return lst


print(timeit.timeit(lambda: my_insertion_sort(lst2), number=1))

# ------------------------------------------------


def quick_sort(s):
    if len(s) < 2:
        return s
    x = s[0]
    return quick_sort([i for i in s[1:] if i < x]) + [i for i in s if i == x] + quick_sort([i for i in s[1:] if i > x])


print(timeit.timeit(lambda: quick_sort(lst3), number=1))

# ------------------------------------------------


def sort_py(lst):
    return lst.sort()


print(timeit.timeit(lambda: sort_py(lst), number=1))


# def sort_py1(lst):
#     return sorted(lst)

# print(timeit.timeit(lambda: sort_py1(lst2), number=1))
