primes = [i for i in range(2, 200)]
for i in range(len(primes)):
    if primes[i]:
        for j in range(i + primes[i], len(primes), primes[i]):
            primes[j] = 0

primes = [i for i in primes if i]

k = 0
# for i in primes:
#     if 3661 <= i * i <= 33625:
#         k += 1

for i in range(3661, 33625 + 1):
    a = i ** .5
    if a == int(a):
        if int(a) in primes:
            k += 1

print(k)
