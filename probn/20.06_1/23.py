tr = [0 for _ in range(16)]
tr[3] = 1

for i in range(16):
    abc = [i + 1, i + 3, i * 2]

    for j in abc:
        if j < 16:
            tr[j] += tr[i]

print(tr)
print(tr[15])
