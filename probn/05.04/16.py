K = 0


def F(n):
    if n > 0:
        G(n - 1)


def G(n):
    global K
    K += 1
    if n > 1:
        K += 1
        F(n - 2)

F(13)
print(K)
