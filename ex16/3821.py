def f(n):
    if n < 2:
        return 1
    else:
        if n % 3 == 0:
            return f(n // 3) + (-1)
        else:
            return f(n - 1) + 17


for i in range(1000000):
    a = f(i)
    if a == 110:
        print(i)




