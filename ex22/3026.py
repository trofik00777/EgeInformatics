for i in range(65, 0, -1):
    x = 65
    y = i
    if (y > x):
        z = x
        x = y
        y = z
    a = x; b = y
    while b > 0:
        r = a % b
        a = b
        b = r
    if a == 13:
        print(i)
        exit()
    # print("%d %d %d" % (a, x, y))
