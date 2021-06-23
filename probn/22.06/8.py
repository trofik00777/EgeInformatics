from itertools import product


word = list("моисей")
k = 0
for i in product(word, repeat=4):
    if i[0] != "й":
        if any(j in i for j in "оие"):
            k += 1

print(k)
