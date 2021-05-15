prost = [i for i in range(2, 10000)]
for i in range(len(prost)):
    if prost[i] > 0:
        for j in range(i + prost[i], len(prost), prost[i]):
            prost[j] = 0


def f(a):
    n = a
    if n % 2 == 0:
        n //= 2
        if n % 2 == 0:
            return False
        else:
            a = n ** .5
            if int(a) == a and int(a) in prost:
                return int(a)

    return False


answ = []
for i in range(113000000, 114000000 + 1, 2):
    a = f(i)
    if a:
        answ.append((i, a))

print(answ)
