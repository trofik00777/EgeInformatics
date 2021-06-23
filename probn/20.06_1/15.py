def check(x, y, a):
    return (2 * y + x < a) or (x > 10) or (y > 25)


for a in range(100):
    fl = True
    for x in range(1, 11):
        for y in range(1, 26):
            if not check(x, y, a):
                fl = False
                break

    if fl:
        print(a)
        break
