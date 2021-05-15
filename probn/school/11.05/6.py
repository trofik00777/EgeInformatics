for i in range(1, 1000):
    s = i
    n = 1
    while n < 21:
        s = s - 1
        n = n + 2

    if s > 600:
        print(i)
        break
