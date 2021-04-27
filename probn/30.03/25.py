def f(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


k = []
for i in range(1532040, 1532161):
    if f(i):
        k.append(i)
k.sort()
print(k)
