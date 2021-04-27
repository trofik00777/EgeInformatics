# +2 +4 +5

a = [0 for i in range(100)]
a[31] = 1

for i in range(31, 100):
    if a[i] == 1001:
        print(i)

    if i + 2 < 100:
        a[i + 2] += a[i]
    if i + 4 < 100:
        a[i + 4] += a[i]
    if i + 5 < 100:
        a[i + 5] += a[i]

print(a)
print(a[56])
