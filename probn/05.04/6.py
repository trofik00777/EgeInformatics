for i in range(1000, 0, -1):
    s = i
    n = 0
    while 400 < s * s:
        s = s - 1
        n = n + 3
    if n < 1000:
        print(i)
        break
