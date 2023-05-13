import timeit
import memory_profiler
import cProfile


# @memory_profiler.profile
def one():
    return list(range(0, 13**6, 2))


print(timeit.timeit(one, number=3))
# cProfile.run('one()')


# @memory_profiler.profile
def one1():
    return [x for x in range(0, 13**6, 2)]


print(timeit.timeit(one1, number=3))
# cProfile.run('one1()')
