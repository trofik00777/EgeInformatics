def F(n):
    if n < 5:
        return F(n + 3) + \
               F(2 * n) + \
               F(3 * n // 2)
    else:
        return n + 2


print(F(3))
