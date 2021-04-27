tr = [0 for i in range(20)]
tr[2] = 1

for i in range(20):
    a = i + 1
    b = i + 3
    c = i * i

    if a < 20:
        tr[a] += tr[i]
    if b < 20:
        tr[b] += tr[i]
    if c < 20:
        tr[c] += tr[i]
print(tr)
print(tr[19])
