def f(n):
    if n <= 18:
        return n + 3
    if n % 3:
        return f(n - 1) + n * n + 5
    else:
        return (n // 3) * f(n // 3) + n - 12


def check(n):
    return all(int(i) % 2 == 0 for i in str(n))


k = 0
for i in range(1, 801):
    if check(f(i)):
        k += 1
print(k)
