def fact(a):
    n = a
    i = 2
    k = []
    while i * i <= n:
        while not n % i:
            k.append(i)
            n //= i
        i += 1
    if n > 1:
        k.append(n)
    print(f"{a}: {k}")
    k = set(k)
    if sum(k) > 250 and not a % sum(k) and len(k) > 1:
        return k
    return False


k = []
for i in range(33333, 55556):
    a = fact(i)
    if a:
        k.append((i, sum(a)))
print(k)
