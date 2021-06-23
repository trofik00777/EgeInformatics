def f(n):
    ch, nch = [], []
    k = []
    i = 2

    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                k.append(i)
            else:
                k.append(i)
                k.append(n // i)

        i += 1

    if len(k) % 2 != 0:
        return False

    for i in k:
        if i % 2 == 0:
            ch.append(i)
        else:
            nch.append(i)

    return len(ch) == len(nch) and len(nch) >= 70


k = []
for i in range(326496, 649632 + 1):
    if f(i):
        k.append(i)
        print(i)

print(k)
