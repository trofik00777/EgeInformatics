tr = [0 for i in range(39)]
tr[2] = 1

for i in range(39):
    a = i + 1
    b = i * 2
    c = i * i

    if a < 39:
        tr[a] += tr[i]
    if b < 39:
        tr[b] += tr[i]
    if c < 39:
        tr[c] += tr[i]
print(tr)
print(tr[38])
