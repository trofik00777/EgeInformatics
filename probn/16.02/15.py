def check(x, y, a):
    if 2 * x + 3 * y < 30 or x + y >= a:
        return True
    return False


for a in range(100, 0, -1):
    fl = True
    for x in range(1000):
        for y in range(1000):
            if not check(x, y, a):
                fl = False
                break
    if fl:
        print(a)
        break
