def F(n):
    global K
    print("*")
    K += 1
    if n > 0:
        G(n - 1)


def G(n):
    global K
    print("*")
    K += 1
    if n > 1:
        F(n - 2)

K = 0
F(13)
print(K)

