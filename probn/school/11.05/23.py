tr = [0 for i in range(13)]
tr[1] = 1

for i in range(13):
    a = i + 1
    b = i + 2
    c = i * 3

    if a < 13:
        tr[a] += tr[i]
    if b < 13:
        tr[b] += tr[i]
    if c < 13:
        tr[c] += tr[i]
print(tr)
print(tr[12])
