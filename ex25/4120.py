def f(n):
    k = 0
    ks = 0
    for i in primes:
        if n % i == 0:
            k += i
            ks += 1

    print(k)
    return k // ks


primes = [i for i in range(2, 700000)]
for i in range(len(primes)):
    if primes[i] > 0:
        for j in range(i + primes[i], len(primes), primes[i]):
            primes[j] = 0
primes = [i for i in primes if i > 0]
print(primes)

k = []
i = 650000
while len(k) < 4 and i < 700000:
    a = f(i)
    if a % 37 == 23:
        k.append((i, a))
        print(i, a)
    i += 1

print(k)
