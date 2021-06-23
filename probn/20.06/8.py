from itertools import permutations

word = list("аспект")
k = 0

for i in permutations(word, r=6):
    if "ае" in "".join(i) or "еа" in "".join(i):
        continue
    k += 1

print(k)
