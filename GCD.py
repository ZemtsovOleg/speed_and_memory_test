import math

print(math.gcd(75, 120))
print(math.lcm(75, 120))


def nod(a, b):
    a = min(a, b)
    b = max(a, b)
    while b > 0:
        a, b = b, a % b
    return a

print(nod(75, 120))


def nok(a, b):
    return a * b // nod(a, b)

print(nok(75, 120))