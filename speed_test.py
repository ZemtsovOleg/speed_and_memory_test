import datetime

# еще мне кажется что первая программа всегда выполнятся чуть дольше
start = datetime.datetime.now()


def one():
    return [x for x in range(13**7) if not x % 2]


one()
print(datetime.datetime.now() - start)


start1 = datetime.datetime.now()


def one1():
    return [x for x in range(13**7) if x % 2 == 0]


one1()
print(datetime.datetime.now() - start1)


start2 = datetime.datetime.now()


def one2():
    return [x for x in range(13**7) if not x % 2]


one2()
print(datetime.datetime.now() - start2)