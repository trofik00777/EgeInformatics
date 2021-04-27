def f(n):
    k = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            k.append(i)
            k.append(n // i)
        i += 1
    k = list(set(k))
    k.sort()
    return len(k), k


k = []
mk = 0
for i in range(586132, 586430 + 1):
    kol, a = f(i)
    if kol > mk:
        k = []
        mk = kol
    if kol == mk:
        k.append((i, a))
k.sort()
print(k[0][0], len(k[0][1]), k[0][1][-2])
print(k[-1][0], len(k[-1][1]), k[-1][1][-2])
