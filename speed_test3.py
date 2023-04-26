import timeit

def one():
    return list(range(0, 13**7, 2))

def one1():
    return [x for x in range(0, 13**7, 2)]


print(timeit.timeit(stmt=one, number=2))
print(timeit.timeit(stmt=one1, number=2))