def check(x, y, a):
    return (y + 2 * x != 48) or (a < x) or (x < y)


for a in range(100, 0, -1):
    fl = True
    for x in range(100):
        for y in range(100):
            if not check(x, y, a):
                fl = False
                break
    if fl:
        print(a)
        break
