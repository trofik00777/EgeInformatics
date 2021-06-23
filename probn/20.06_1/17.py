k = []
for i in range(-9563, -3102 + 1):
    if i % 7 == 0 and i % 11 and i % 23 and str(i)[-1] != "8":
        k.append(i)

print(k)
print(len(k))
print(max(k))
