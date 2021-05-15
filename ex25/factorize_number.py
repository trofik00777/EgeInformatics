def fact(a):
    n = a
    p = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            p.append(i)
            n //= i
        i += 1
    if n > 1:
        p.append(n)

    return p


print(fact(103018658))
