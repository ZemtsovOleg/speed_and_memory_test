import random
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

lst = [random.randint(-10000, 10000) for _ in range(50000)]
lst1 = lst[:]
lst2 = lst[:]
lst3 = lst[:]

# #------------------------------------------------

# @decorator_time
# def sort_my(lst):
#     for index in range(len(lst) - 1):
#         count = index + 1
#         while count < len(lst):
#             if lst[index] > lst[count]:
#                 lst[index], lst[count] = lst[count], lst[index]
#             else:
#                 count += 1
#     return lst

# sort_my(lst)

# #------------------------------------------------

# @decorator_time
# def bubble_sort(lst):
#     for x in range(l := len(lst)):
#         done = True
#         for i in range(l - 1 - x):
#             if lst[i] > lst[i+1]:
#                 lst[i], lst[i+1] = lst[i+1], lst[i]
#                 done = False
#         if done:
#             break
#     return lst

# bubble_sort(lst1)

# #------------------------------------------------

# @decorator_time
# def my_insertion_sort(lst):
#     for i in range(1, len(lst)):
#         if lst[i] < lst[i-1]:
#             for y in range(len(lst[0:i])):
#                 if lst[i] < lst[y]:
#                     lst[i], lst[y] = lst[y], lst[i]
#     return lst

# my_insertion_sort(lst1)

#------------------------------------------------

# start = datetime.datetime.now()
# def quick_sort(s):
#     if len(s) < 2:
#         return s
#     x = s[0]
#     return quick_sort([i for i in s[1:] if i < x]) + [i for i in s if i == x] + quick_sort([i for i in s[1:] if i > x])

# quick_sort(lst)
# print(datetime.datetime.now() - start)

#------------------------------------------------

@decorator_time
def sort_py(lst):
    return lst.sort()

sort_py(lst2)

@decorator_time
def sort_py1(lst):
    return sorted(lst)

sort_py1(lst3)