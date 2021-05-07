def f(a, k_div):
    n = a
    k = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                k += 1
            else:
                k += 2
        i += 1

    if k > k_div:
        return k
    return False


answ = []
div = -1
i = 700000
while len(answ) < 5:
    a = f(i, div)
    if a:
        div = a
        answ.append((i, a))
    else:
        answ = []
        div = -1
    i += 1
    if i % 1000 == 0:
        print(i)
print(answ)
