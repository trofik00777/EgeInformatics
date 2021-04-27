def f(n):
    if n == 1:
        return 1
    return f(n - 1) + 3 * g(n - 1)


def g(n):
    if n == 1:
        return 1
    return f(n - 1) - 2 * g(n - 1)


print(f(18))
