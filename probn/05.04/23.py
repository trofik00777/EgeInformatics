tr = [0 for _ in range(50)]
tr[5] = 1

for i in range(50):
    a = i + 1
    b = i * 3

    if a < 50:
        tr[a] += tr[i]
    if b < 50:
        tr[b] += tr[i]

print(tr)
print(tr[49])
