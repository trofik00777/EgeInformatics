def f(n):
    if n <= 3:
        return n
    if n % 2:
        return n * n + f(n - 2)
    else:
        return n + f(n - 1)


k = 0
for i in range(1, 1000):
    a = f(i)
    if a >= 10 ** 8:
        print(k)
        exit()
    k += 1
