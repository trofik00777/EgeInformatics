def check(x, y, a):
    return (3 * y + 2 * x != 130) or (3 * x > a) or (2 * y > a)


for a in range(1000, 0, -1):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not check(x, y, a):
                flag = False
                break
    if flag:
        print(a)
        exit()
