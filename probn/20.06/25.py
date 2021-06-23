def cifrs(n):
    s = 0
    m = 1
    for i in str(n):
        a = int(i)
        s += a
        m *= a
    return (s, m)


k = []
for i in range(87921, 88187 + 1):
    s, m = cifrs(i)
    if s % 14 == 0:
        if m and m % 18 == 0:
            k.append((i, s, m))

k.sort(key=lambda x: x[-1])
for i in k:
    print(*i[1:])
