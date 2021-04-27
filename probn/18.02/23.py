tr = [0 for _ in range(33)]
tr[1] = 1

for i in range(len(tr)):
    a, b = i + 1, i * 4

    if a < len(tr):
        tr[a] += tr[i]

    if b < len(tr):
        tr[b] += tr[i]
print(tr)
print(tr[32])
