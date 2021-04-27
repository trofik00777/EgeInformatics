k = []

for i in range(3394, 8600):
    if i % 3 == 1 and i % 7 == 5:
        k.append(i)

print(max(k))
print(sum(k))
