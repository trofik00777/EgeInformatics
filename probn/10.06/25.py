def f(n):
    k = [1, n]
    i = 2
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                k.append(i)
            else:
                k.append(i)
                k.append(n // i)
        i += 1
    return k[:]


k = []
for i in range(222987, 223021 + 1):
    a = f(i)
    if len(a) == 4:
        a.sort()
        k.append((a[-2], a[-1]))

for i in k:
    print(*i)
