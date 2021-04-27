from itertools import product, permutations

d = set("приказ")

k = 0
for i in permutations(d, 4):
    print(i)
    if i.count("и") + i.count("а") < 2:
        k += 1
print(k)
