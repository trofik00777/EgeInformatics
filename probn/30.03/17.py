k = []
for i in range(1606, 9681):
    if i % 11 == 0 and i % 7 and i % 13 and i % 17 and i % 19:
        k.append(i)
print(len(k))
print(max(k))
