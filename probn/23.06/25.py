PRIMES = [i for i in range(2, 100000)]
for i in range(len(PRIMES)):
    a = PRIMES[i]
    if a > 0:
        for j in range(i + a, len(PRIMES), a):
            PRIMES[j] = 0

PRIMES = [i for i in PRIMES if i]



def f(n):
    a = n ** .25
    if int(a) == a:
        if int(a) in PRIMES:
            return True

    return False



k = 0
m = -1
for i in range(125873, 136762 + 1):
    if f(i):
        k += 1
        m = i

print(k, m)
