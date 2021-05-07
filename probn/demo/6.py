for i in range(100, 0, -1):
    s = i
    n = 1
    while s < 47:
        s = s + 4
        n = n * 2
    if n == 64:
        print(i)
        break
