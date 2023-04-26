def div_con(lst):
    result = 0
    for i in lst:
        if isinstance(i, int):
            result += i
        else:
            result -= int(i)
    return result

print(div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']))


# это решение должно быть быстрее 
def div_con1(lst):
    return sum(n if isinstance(n, int) else -int(n) for n in lst)