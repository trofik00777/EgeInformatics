k = []
for i in range(980, 5320 + 1):
    if (i % 4 == 0 or i % 5 == 0) and i % 11 and i % 17 and i % 19 and i % 23:
        k.append(i)

print(len(k), min(k))
# 1353 980
