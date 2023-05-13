import timeit

code_to_test = """
users_buy = [
    ('confirmed', 100),
    ('unconfirmed', 200),
    ('unconfirmed', 400),
    ('confirmed', 600)
]

def cycle_example():
    res = 0
    for user in users_buy:
        if user[0] == 'confirmed':
            res += user[1]
    return res

cycle_example()
"""

print(timeit.timeit(code_to_test, number=100000))
