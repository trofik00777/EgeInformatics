from itertools import product

word = list("берклий")
k = 0

for i in product(word, repeat=4):
    if i[0] != "й":
        if "е" in i or "и" in i:
            k += 1

print(k)
