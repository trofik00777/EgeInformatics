def check(a):
    n = a
    i = 2
    k = []

    while i * i <= n:
        while n % i == 0:
            k.append(i)
            n //= i

        i += 1

    if n > 1:
        k.append(n)

    return k


k = []
for i in range(268312, 336492 + 1):
    a = check(i)
    if len(a) == 2 == len(set(a)):
        k.append(i)

print(k)
print(len(k))
print(min(k))
