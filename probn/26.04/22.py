for i in range(1, 1000):
    x = i
    a = 0
    b = 0
    while x > 0:
        if x % 2 == 0:
            a += 1
        else:
            b += x % 4
        x = x // 4
    if a == 1 and b == 5:
        print(i)
        break
