tr = [0 for _ in range(21)]
tr[10] = 14

for i in range(21):
    a = i + 1
    b = i * 2

    if a < 21:
        tr[a] += tr[i]
    if b < 21:
        tr[b] += tr[i]
print(tr)
print(tr[20])
