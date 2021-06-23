k = 0

for i in range(100, 1000):
    n = str(i)
    a, b, c = sorted(map(int, list(n)))

    ma = int(str(c) + str(b))
    if a == 0:
        mi = int(str(b) + str(a))
    else:
        mi = int(str(a) + str(b))

    r = ma - mi
    if r == 35:
        k += 1
        print(i)

print(k)
