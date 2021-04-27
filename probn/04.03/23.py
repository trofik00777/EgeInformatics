tr = [0 for _ in range(41)]
tr[2] = 1


for i in range(41):
    a = i + 2
    b = i * 2

    if a < 41:
        tr[a] += tr[i]
    if b < 41:
        tr[b] += tr[i]
print(tr)
print(tr[40])
