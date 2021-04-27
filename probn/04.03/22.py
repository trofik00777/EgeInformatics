for i in range(201, 1000):
    x = i
    L = 2 * x - 20
    M = 2 * x + 30
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if M == 50:
        print(i)
        exit()
