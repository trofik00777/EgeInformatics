def f(n):
    if n == 1:
        return 1
    if n % 2:
        return 2 * f(n - 2)
    else:
        return n + f(n - 1)

print(f(26))
