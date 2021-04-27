import math


PROST = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def f(a):
    n = a
    while n % 2 == 0:
        n //= 2
    b = math.sqrt(math.sqrt(n))
    if b == int(b) and int(b) in PROST:
        return a, b ** 4
    return False


k = []
for i in range(63000000, 75000000 + 1):
    a = f(i)
    if i % 1000 == 0:
        print(i)
    if a:
        k.append(a)

print(k)
# print(math.sqrt(289))
print(289**0.5)
