def check(x, y, a):
    return (x * y < 2 * a) or (x >= 11) or (x < 2 * y)


for a in range(1000):
    fl = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not check(x, y, a):
                fl = False
                break

    if fl:
        print(a)
        exit()
