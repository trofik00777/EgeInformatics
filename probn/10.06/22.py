for i in range(10000, 0, -1):
    x = i
    L = 0
    M = 0
    while x > 0:
        L = L + 1
        if x % 2 == 0:
            M = M + (x % 10) // 2
        x = x // 10

    if L == 3 and M == 7:
        print(i)
        break
    # print("%d\n%d" % (L, M))  # 3 7
