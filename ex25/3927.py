from itertools import product, permutations


prost = [i for i in range(2, 29)]
for i in range(len(prost)):
    if prost[i] > 0:
        for j in range(i + prost[i], len(prost), prost[i]):
            prost[j] = 0
prost = [i for i in prost if i > 0]
print(prost[:])
print(len(prost))

s = 1
for i in prost[:2]:
    s *= i
print(s*8)


def f(a):
    n = a
    k = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                k += 1
            else:
                k += 2
        i += 1

    return k


print(f(17297280))
