def f(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False

        i += 1

    return True


k = []
for i in range(2532007, 2532160 + 1, 10):
    if f(i):
        k.append(i)

for ind, i in enumerate(k):
    print(ind + 1, i)








