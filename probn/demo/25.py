def f(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                return 0
            return i + n // i
        i += 1
    return 0


k = []
a = 452022
while len(k) < 5:
    m = f(a)
    if m % 7 == 3:
        k.append((a, m))
    a += 1
print(k)
