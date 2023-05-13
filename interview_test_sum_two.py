import random
import datetime

mas = [random.randint(-100000, 100000) for _ in range(9000)]
# mas = [-5,20,15,1,1,-10,2,3,4,5,30,6,7,8,9]

# первая программа как заглушка так как на мой взгляд создание списка сильно нагружает систему 
# программа ищет два числа из массива которые в сумме дадут n число или максимально близкое к нему 
#-----------------------------------------------------------------

start = datetime.datetime.now()
def twosum(mas: list[int], n: int)-> list[int]:
    mas.sort()
    l, r = 0, len(mas)-1
    while l < r:
        temp = mas[l] + mas[r]
        if temp == n:
            return [mas[l], mas[r]]
        if r - l == 1:
            return [mas[l], mas[r]]
        if temp < n:
            l += 1
        else:
            r -= 1

print(twosum(mas, 100))
print(datetime.datetime.now() - start)

#--------------------------------------------------------
# тут мы создаем переменную lst и каждый раз записываем м него значения, чтобы не потерять последние 

start1 = datetime.datetime.now()
def twosum1(mas: list[int], n: int)-> list[int]:
    mas.sort()
    l, r = 0, len(mas)-1
    while l < r:
        temp = mas[l] + mas[r]
        lst = [mas[l], mas[r]]
        if temp == n:
            return lst
        if temp < n:
            l += 1
        else:
            r -= 1
    return lst

print(twosum1(mas, 100))
print(datetime.datetime.now() - start1)

#-----------------------------------------------------------------
#  тут мы создаем if вместо пременной lst 

start2 = datetime.datetime.now()
def twosum2(mas: list[int], n: int)-> list[int]:
    mas.sort()
    l, r = 0, len(mas)-1
    while l < r:
        temp = mas[l] + mas[r]
        if temp == n:
            return [mas[l], mas[r]]
        if r - l == 1:
            return [mas[l], mas[r]]
        if temp < n:
            l += 1
        else:
            r -= 1

print(twosum2(mas, 100))
print(datetime.datetime.now() - start2)