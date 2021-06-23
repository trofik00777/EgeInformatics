tr = [0 for _ in range(16)]
tr[3] = 1

for i in range(16):
    a = i + 1
    b = i + 2
    c = i + 3

    if a < 16 and a != 8:
        tr[a] += tr[i]
    if b < 16 and b != 8:
        tr[b] += tr[i]
    if c < 16 and c != 8:
        tr[c] += tr[i]
print(tr)
print(tr[15])
