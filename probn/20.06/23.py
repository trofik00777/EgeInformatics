tr = [0 for i in range(43)]
tr[3] = 1

for i in range(43):
    a = i + 3
    b = i * 2

    if a < 43:
        tr[a] += tr[i]
    if b < 43:
        tr[b] += tr[i]

print(tr)
print(tr[42])
