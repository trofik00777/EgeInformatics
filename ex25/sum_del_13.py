def check(n):
    i = 2
    divs = 0
    while i * i < n:
        if n % i == 0:
            divs += i
            divs += n // i
        i += 1
    if i * i == n:
        divs += i

    return divs


k = []
i = 350301
while len(k) < 6:
    a = check(i)
    if a % 13 == 0:
        k.append((i, a // 13))
    i += 1

print(k)
