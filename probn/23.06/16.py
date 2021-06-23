def F(n):
    global K, L
    # print(2 * n + 1)
    K += 2 * n + 1
    # L += 1
    # if L > 1000:
    #     return

    if n > 1:
        # print(3 * n - 8)
        K += 3 * n - 8

        F(n - 1)
        F(n - 4)


K = 0
L = 0
for i in range(1000):
    K = 0
    L = 0
    F(i)
    print("----------------------------------------------------")
    # print(K)
    if K > 5000000:
        print(i, K)
        break



