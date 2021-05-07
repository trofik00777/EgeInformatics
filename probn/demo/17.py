k = []
for i in range(16015, 48989 + 1):
    if (i % 7 == 0 or i % 11 == 0) and i % 9 != 0 and i % 12 != 0 and i % 13 != 0:
        k.append(i)

print(len(k))
print(min(k))
