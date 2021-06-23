def f(x, a):
    return (x & 87 != 0) or ((x & 31 == 0) or (x & a != 0))


for a in range(1000):
    fl = True
    for x in range(1, 100):
        if not f(x, a):
            fl = False
            break
    if fl:
        print(a)
        break

