K = 0


def F(n):
    global K
    print("*")
    K += 1
    if n > 0:
        print("*")
        K += 1
        G(n - 1)


def G(n):
    global K
    print("*")
    K += 1
    if n > 1:
        print("*")
        K += 1
        F(n - 2)


F(12)
print(K)
