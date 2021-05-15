def f(n):
    if n > 30:
        return n * n + 3 * n + 5

    if n % 2 == 0:
        return 2 * f(n + 1) + f(n + 4)
    else:
        return f(n + 2) + 3 * f(n + 5)



k = 0
for i in range(1, 1001):
    a = str(f(i))
    if a.count("0") >= 2:
        k += 1

print(k)
