for i in range(10000):
    s = i
    n = 127
    while s - n > 0:
        s = s + 15
        n = n + 20

    if len(str(s)) == 4:
        print(i)
        break
