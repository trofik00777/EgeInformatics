for i in range(10000, 100000):
    x = i
    a = 0
    b = 0
    y = 1
    while x > 0:
        if (x % 10) % 2 == 0:
            a = a * 10 + x % 10
        else:
            y = y * 10
            b = b * 10 + x % 10
        x = x // 10
    a = a * y + b

    if a == 26391:
        print(i)
        break
