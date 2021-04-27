def f(n):
    if n <= 5:
        return n + 15

    if n % 2:
        return f(n - 1) + 2 * n * n + 1
    else:
        return f(n // 2) + n * n * n - 1


def check(n):
    a = str(n).count("8")
    return a >= 2


k = 0
for i in range(1, 1001):
    if check(f(i)):
        k += 1
print(k)
