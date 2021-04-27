k = []
for i in range(1361, 7724 + 1):
    if i % 2 == 0 and i % 19:
        k.append(i)
print(len(k))
print(sum(k))
