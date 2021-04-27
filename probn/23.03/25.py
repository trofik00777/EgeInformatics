def fact(a):
    n = a
    i = 2
    k = []
    while i * i <= n:
        while n % i == 0:
            k.append(i)
            n //= i
        i += 1
    if n > 1:
        k.append(n)
    if len(k) == 2 == len(set(k)):
        return k[-1] - k[0]
    return -1


k = []
for i in range(523456, 578926):
    a = fact(i)
    if a != -1:
        k.append((a, i))
print(k)
print(min(k))
