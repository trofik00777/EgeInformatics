tr = [0 for _ in range(66)]
tr[1] = 1

for i in range(65):
    a = i + 1
    b = i * 3
    if a < 66:
        tr[a] += tr[i]
    if b < 66:
        tr[b] += tr[i]
k = tr[20]
tr = [0 for _ in range(66)]
tr[20] = k

for i in range(65):
    a = i + 1
    b = i * 3
    if a < 66:
        tr[a] += tr[i]
    if b < 66:
        tr[b] += tr[i]
print(tr)
print(tr[65])
