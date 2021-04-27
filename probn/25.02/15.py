def check(x, a):
    return x % a or x % 36 == 0 or x % 12


for a in range(1, 10000):
    fl = True
    for x in range(1, 100):
        if not check(x, a):
            fl = False
            break
    if fl:
        print(a)
        exit()
