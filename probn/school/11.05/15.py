def check(x, a):
    return x % a != 0 or (x % 34 == 0 and x % 51 == 0)


for a in range(1, 1000):
    fl = True
    for x in range(1, 150):
        if not check(x, a):
            fl = False
            break
    if fl:
        print(a)
        break
