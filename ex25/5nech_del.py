prost = [i for i in range(2, 200)]
for i in range(len(prost)):
    if prost[i] != 0:
        k = prost[i]
        for j in range(i + k, len(prost), k):
            prost[j] = 0
print(prost)


def check(a):
    n = a
    while n % 2 == 0:
        n //= 2

    n4 = n ** .25
    if int(n4) == n4 and int(n4) in prost:
        return int(n4)
    return False


k = []
for i in range(77777777, 88888888 + 1):
    a = check(i)
    if a:
        k.append((i, a))

print(k)
