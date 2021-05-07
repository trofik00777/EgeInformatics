tr = [0 for _ in range(24)]
tr[23] = 1

for i in range(23, -1, -1):
    a = i - 2
    b = i - 5

    if a >= 0:
        tr[a] += tr[i]
    if b >= 0:
        tr[b] += tr[i]
print(tr)
print(tr[2])
