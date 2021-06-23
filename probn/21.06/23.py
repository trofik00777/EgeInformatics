tr = [0 for _ in range(20)]
tr[1] = 1

for i in range(20):
    abc = [i + 1, i * 2, i * 3]

    for j in abc:
        if j < 20:
            tr[j] += tr[i]

print(tr)
print(tr[18])
