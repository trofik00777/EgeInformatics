def check(n):
    k = []
    for i in range(2, n):
        if n % i == 0:
            k.append(i)
    if len(k) == 2:
        return k


for i in range(174457, 174505):
    a = check(i)
    if a:
        print(a)
