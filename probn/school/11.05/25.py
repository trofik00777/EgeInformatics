def f(n):
    k = []
    i = 1
    while i * i < n:
        if n % i == 0:
            k.append(i)
            k.append(n // i)
        i += 1
    if i * i == n:
        k.append(i)

    k.sort()
    if len(k) == 6:
        return (k[-2], k[-1])
    return False


k = []
for i in range(180131, 180179 + 1):
    a = f(i)
    if a:
        k.append(a)

print(k)
