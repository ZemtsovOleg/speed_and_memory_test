import cProfile
import memory_profiler


def one():
    return list(range(999999))

cProfile.run('one()')


@memory_profiler.profile
def one1():
    return list(range(999999))

one1()


print(one.__sizeof__())
