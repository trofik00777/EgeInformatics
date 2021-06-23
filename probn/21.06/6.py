for i in range(1000):
    s = i
    n = 0
    while s < s * s:
        s = s - 1
        n = n + 3

    if n > 2000:
        print(i)
        break
