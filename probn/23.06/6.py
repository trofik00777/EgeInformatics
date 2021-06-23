for i in range(100000, 0, -1):
    n = i
    s = 350
    while 2 * s + n < 1100:
        s = s - 5
        n = n + 15

    if s == 45:
        print(i)
        break



