k = []
for i in range(5913, 11753 + 1):
    if i % 5 == 0 and i % 11 == 0 and i % 7 and i % 10 and i % 13 and i % 22:
        k.append(i)

print(k)
print(len(k))
print(k[0])
