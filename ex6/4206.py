for i in range(1000):
    x = i
    k = 0
    while x < 100:
        k += 1
        if x % 2 < 1:
            x = x // 2
        else:
            x = 3 * x + 1
        if k > 1000:
            break
    else:
        print(i)
