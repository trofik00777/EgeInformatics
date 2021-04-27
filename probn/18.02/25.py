def check(n):
    k = []
    for i in range(2, n):
        if n % i == 0:
            k.append(i)
    return k


k = dict()

for i in range(586132, 586431):
    a = check(i)
    len_a = len(a)

    if len_a in k:
        k[len_a].append((i, a))
    else:
        k[len_a] = [(i, a)]
b = max(k.keys())
print(b)
print(k[b])
print(max(k[b]))
print(min(k[b]))
