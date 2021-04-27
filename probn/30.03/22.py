for i in range(10000, 0, -1):
    x = i
    a = 0
    b = 0
    while x > 0:
        a = a + 1
        b = b + (x % 100)
        x = x // 100
    if a == 2 and b == 15:
        print(i)
        break
    # print("%d\n%d" % (a, b))
