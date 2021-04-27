# +1 +2 *3  5->26  in 11  not in 13,15
a = [0 for i in range(26+1)]
a[5] = 1
for i in range(5, 11):
    if i + 1 < 12:
        a[i + 1] += a[i]
    if i + 2 < 12:
        a[i + 2] += a[i]
    if i * 3 < 12:
        a[i * 3] += a[i]

for i in range(11, len(a)):
    if i + 1 < 27 and i + 1 != 13 and i + 1 != 15:
        a[i + 1] += a[i]
    if i + 2 < 27 and i + 2 != 13 and i + 2 != 15:
        a[i + 2] += a[i]
    if i * 3 < 27 and i * 3 != 13 and i * 3 != 15:
        a[i * 3] += a[i]

print(a)
print(a[26])
