k = []

for i in range(2848, 109499 + 1):
    a = str(i)
    if "9" in a:
        s = sum(int(j) for j in a if int(j) > 5)

        if s % 3 == 0:
            k.append(i)

print(k)
print(len(k))
print(max([i for i in k if str(i)[0] == "8"]))
