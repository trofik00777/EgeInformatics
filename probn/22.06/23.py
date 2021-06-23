tr = [0 for _ in range(17)]
tr[14] = 279

for i in range(17):
    a = i + 1
    b = i + 2
    c = i * 3

    if a < 17:
        tr[a] += tr[i]
    if b < 17:
        tr[b] += tr[i]
    if c < 17:
        tr[c] += tr[i]

print(tr)
print(tr[16])


