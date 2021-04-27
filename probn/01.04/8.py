from itertools import product, permutations


d = set("азимут")
sogl = list("змт")
k = 0
for i in product(d, repeat=6):
    a = "".join(i)
    r = 0
    for j in a:
        if j in sogl:
            r += 1
    if r >= 3:
        k += 1
print(k)
