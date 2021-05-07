def f(n, divs):
    k = 2
    i = 2
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                k += 1
            else:
                k += 2
        i += 1

    if k > divs:
        return k
    return False


answ = []
divss = 0
i = 700000
while len(answ) < 5:
    a = f(i, divss)
    if a:
        divss = a
        answ.append((i, a))
    i += 1
print(answ)
