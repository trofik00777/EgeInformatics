K = 0


def F(n):
    global K
    if n < 3:
        K += 1
        print("*")
    else:
        F(n - 1)
        F(n - 2)
        F(n - 2)

F(6)
print(K)
