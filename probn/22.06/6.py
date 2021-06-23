for i in range(1000):
    s = i
    n = 10
    while s > n + 20:
        s = s - 6
        n = n + 11

    if n >= 450:
        print(i)
        break
