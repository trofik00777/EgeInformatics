tr = [0 for _ in range(45)]
for i in range(10, 45):
    a = i + 7
    b = i - 4

    if a < 45:
        tr[a] += tr[i]
    if b > 0:
        tr[b] += tr[i] + 1
print(tr)
