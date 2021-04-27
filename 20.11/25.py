def f(n):
    k = []
    for j in range(2, n):
        if not n % j:
            k.append(j)
    return k


for i in range(174457, 174506):
    k = f(i)
    if len(k) == 2:
        print(i, k)
