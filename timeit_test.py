import time


def func():
    start = time.perf_counter()
    # часть кода
    print(f'{time.perf_counter() - start}')
    start2 = time.perf_counter()
    # часть кода
    print(f'{time.perf_counter() - start2}')
    return None


func()

# --------------------------------------------

read = 1
write = 2
execute = 4

# это запись занимает всего один байт, в одном байте мы можем сразу хранить несколько параметров
user = read | write | execute

print(user)