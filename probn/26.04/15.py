def check(x, a):
    return (x % a != 0 or x % 16 != 0) or x % 16 != 0 or x % 24 == 0


for a in range(1, 1000):
    fl = True
    for x in range(1, 1000):
        if not check(x, a):
            fl = False
            break

    if fl:
        print(a)
        break
