for i in range(1, 1000):
    s = i
    n = 127
    while s - n > 0:
        s = s + 15
        n = n + 20

    if len(str(s)) == 4:
        print(i)
        break
