tr = [0 for _ in range(19)]
tr[1] = 1

for i in range(19):
    a = i + 1
    b = i + 3
    c = i * 4

    if a < 19:
        tr[a] += tr[i]
    if b < 19:
        tr[b] += tr[i]
    if c < 19:
        tr[c] += tr[i]
print(tr)
print(tr[18])
