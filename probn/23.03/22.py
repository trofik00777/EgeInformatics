for i in range(101, 1000):
    x = i
    L = x - 21
    M = x + 12
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if M == 11:
        print(i)
        break
