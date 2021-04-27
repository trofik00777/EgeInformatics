def check(n):
    k = []
    for i in range(1, n):
        if n % i == 0:
            k.append(i)
    if sum(k) == n:
        return len(k)
    else:
        return False


k = []
for i in range(2, 10001):
    a = check(i)
    if a:
        k.append((i, a))
print(k)
