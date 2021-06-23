k = []

for i in range(15000, 25000 + 1):
    if sum(1 for j in [7, 11, 17, 19] if i % j == 0) == 2:
        k.append(i)

print(k)
print(len(k))
print(max(k))
