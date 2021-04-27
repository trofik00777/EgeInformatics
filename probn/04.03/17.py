k = []
for i in range(1325, 15367):
    if i % 13 == 0 and i % 7 and i % 17 and i % 19 and i % 23:
        k.append(i)
print(len(k))
print(min(k))
