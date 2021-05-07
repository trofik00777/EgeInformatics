from itertools import product


alf = set("вишня")
k = 0
for i in product(alf, repeat=6):
    if i.count("в") < 2 and i[0] != "ш" and i[-1] not in ["и", "я"]:
        k += 1
print(k)
