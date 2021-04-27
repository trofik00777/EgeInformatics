def f(n):
    i = 1
    k = 0
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                k += 1
            else:
                k += 1
                a = n // i
                if a % 2:
                    k += 1
        i += 2
    return k == 5


k = []
for i in range(105000000, 115000000 + 1):
    if i % 1000 == 0:
        print(i)
    if f(i):
        k.append(i)
print(k)
