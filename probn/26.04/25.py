def f(a):
    n = a
    i = 2
    while i * i <= n:
        if n % (i * i) == 0:
            return False
        i += 1
    return sum(map(int, str(a)))


k = []
for i in range(2945, 18294 + 1):
    a = f(i)
    if f(i):
        k.append(a)
print(sum(k))
