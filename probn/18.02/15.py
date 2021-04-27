def check(x, a):
    return x % a == 0 or x % 6 == 0 or x % 3


for a in range(100, 0, -1):
    fl = True
    for x in range(100):
        if not check(x, a):
            fl = False
    if fl:
        print(a)
        exit()
