def f(x, y, a):
    return (3 * y + 2 * x != 130) or (3 * x > a) or (2 * y > a)


for a in range(500, 0, -1):
    fl = True
    for x in range(1, 200):
        for y in range(1, 100):
            if not f(x, y, a):
                fl = False
                break
    if fl:
        print(a)
        exit()
