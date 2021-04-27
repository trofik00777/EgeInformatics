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
    print(f"{a}: {k} {len(k) == len(set(k))}")
    if len(k) == len(set(k)):
        return sum(int(i) for i in str(a))
    return 0


k = []
for i in range(2945, 18295):
    k.append(fact(i))
print(k)
print(sum(k))
