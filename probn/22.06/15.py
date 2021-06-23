def f(x, y, a):
    return (2 * x + 3 * y != 72) or ((a > x) and (a > y))


for a in range(100):
    fl = True
    for x in range(100):
        for y in range(100):
            if not f(x, y, a):
                fl = False
                break

    if fl:
        print(a)
        break

