def f(x, y, a):
    return ((x - 20 < a) and (10 - y < a)) or ((x + 4) * y > 45)


for a in range(1000):
    fl = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not f(x, y, a):
                fl = False
                break
    if fl:
        print(a)
        break
