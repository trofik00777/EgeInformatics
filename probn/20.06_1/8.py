from itertools import permutations


word = list("комбайн")
k = 0

for i in permutations(word, r=7):
    if i[0] != "й" and "ай" not in "".join(i):
        k += 1
        print("".join(i))

print(k)
