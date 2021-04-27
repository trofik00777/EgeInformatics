k = []

for i in range(1871, 9198):
    if i % 9 == 2 or i % 9 == 4:
        if not 16 ** 3 <= i < 16 ** 4:
            k.append(i)

print(k)
print(len(k))
print(min(k))
