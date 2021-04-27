def f(n):
    if n <= 3:
        return n
    if n % 2 == 0:
        return 2 * n + f(n - 1)
    else:
        return n * n + f(n - 2)


k = []
for i in range(1, 101):
    a = f(i)
    if a % 3 == 0:
        k.append(i)
print(k)
print(len(k))
