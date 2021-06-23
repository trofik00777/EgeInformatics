PRIMES = [i for i in range(2, int(50_000_000 ** .25) + 10)]
for i in range(len(PRIMES)):
    a = PRIMES[i]
    if a > 0:
        for j in range(i + a, len(PRIMES), a):
            PRIMES[j] = 0
PRIMES = set(i for i in PRIMES if i > 0)


def check(a):
    n = a
    while n % 2 == 0:
        n //= 2

    a = n ** .25
    if int(a) == a:
        if int(a) in PRIMES:
            return True

    return False


answ = []
for i in range(45_000_000, 50_000_000 + 1):
    if check(i):
        answ.append(i)

print(*answ, sep="\n")
