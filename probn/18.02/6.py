for i in range(1000, 0, -1):
    s = i
    n = 200
    while s // n >= 2:
        s = s + 5
        n = n + 5
    if len(str(s)) == 3:
        print(i)
        exit()
