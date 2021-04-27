def f(n):
    if n <= 15:
        return n * n + 3 * n + 9
    if n % 3:
        return f(n - 2) + n + 2
    else:
        return f(n - 1) + n - 2


k = 0
for i in range(1, 1001):
    a = f(i)
    if all(int(j) % 2 == 0 for j in str(a)):
        k += 1
print(k)
