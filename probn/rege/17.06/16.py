def F(n):

    if n > 0:

        F(n - 3)

        print(n)

        F(n // 3)


F(9)
