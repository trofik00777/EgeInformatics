def check(x, y, a):
    return (x * y < 3 * a) or (x >= 31) or (x < 5 * y)


for a in range(1, 1000):
    fl = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not check(x, y, a):
                fl = False
                break
    if fl:
        print(a)
        break
