for i in range(101, 1000):
    x = i
    L = x - 12
    M = x + 12
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if M == 2:
        print(i)
        exit()
