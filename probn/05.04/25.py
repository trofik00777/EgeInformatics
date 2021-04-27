def f(a):
    n = a
    i = 1
    k = []
    while i * i <= n:
        if n % i == 0:
            k.append(i)
            k.append(n // i)
        i += 1
    k = list(set(k))
    if len(k) == 4:
        k.sort()
        return k[-2:]
    return False


k = []
for i in range(194455, 194500 + 1):
    a = f(i)
    if a:
        k.append(a)

for i in k:
    print(i[0], i[1])
