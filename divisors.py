# import datetime

def divisors(integer):
    i = 2
    dividers = []
    while i * i <= integer:
        if not integer % i:
            dividers.append(i)
            if i != integer // i:
                dividers.append(integer // i)
        i += 1
    return sorted(dividers) or f'{integer} is prime'

print(divisors(15), [3,5])
print(divisors(253), [11,23])
print(divisors(24), [2,3,4,6,8,12])   
print(divisors(25), [5])
print(divisors(13), "13 is prime")
print(divisors(3), "3 is prime")
print(divisors(29), "29 is prime")


# start = datetime.datetime.now()
# def divisors2(integer):
#     i = 2
#     dividers = []
#     while i * i <= integer:
#         if not integer % i:
#             dividers.append(i)
#             if i != integer // i:
#                 dividers.append(integer // i)
#         i += 1
#     return sorted(dividers) or f'{integer} is prime'

# divisors2(99999999)
# print(datetime.datetime.now() - start)

# # медленный 
# start = datetime.datetime.now()
# def divisors1(integer):
#     return [n for n in range(2, (integer // 2) + 1) if not integer % n] or f'{integer} is prime'

# divisors1(99999999)
# print(datetime.datetime.now() - start)