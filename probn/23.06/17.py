k = []
for i in range(10, 1178):
    if i % 2 == 0:
        a = str(i)
        if a[-1] not in ["0", "2", "6", "8"] and a[-2:] != "14":
            k.append(i)

print(sum(k))
print(min(k))



