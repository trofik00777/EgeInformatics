def check(n):
    k = []
    for i in range(1, n + 1):
        if n % i == 0:
            k.append(i)
    if len(k) == 4:
        return k[2:]
    return False


for i in range(251811, 251827):
    a = check(i)
    if a:
        print(a)
