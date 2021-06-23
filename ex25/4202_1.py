primes = [i for i in range(2, 10000000)]
for i in range(10000000 // 2 + 5):
    if primes[i]:
        for j in range(i + primes[i], 10000000 - 2, primes[i]):
            primes[j] = 0

pr = [i for i in primes[3000000 - 2:] if i]
pairs = []
for i in range(1, len(pr)):
    if pr[i] == pr[i - 1] + 2:
        pairs.append(pr[i - 1] + pr[i])

print(len(pairs))
print(pairs[-1] // 2)
