n = 31
tr = [0 for _ in range(n)]
tr[21] = 1

for i in range(n):
    a = i + 1
    b = i + 3
    c = i + 6

    if a < n:
        tr[a] += tr[i]
    if b < n:
        tr[b] += tr[i]
    if c < n:
        tr[c] += tr[i]
print(tr)
print(tr[30])
