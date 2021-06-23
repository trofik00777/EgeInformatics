from itertools import product

word = list(sorted(list("инставк")))
k = 0

for i in product(word, repeat=4):
    a = "".join(i)
    if a == "ника":
        k += 1
        print(k)
        break
    else:
        if a[0] in "нствк":
            if a[-1] in "иа":
                k += 1

