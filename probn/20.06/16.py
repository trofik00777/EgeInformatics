def f(n):
    if n <= 1:
        return 2

    return f(n - 1) + f(n - 2) + 2 * n + 4


print(f(25))
