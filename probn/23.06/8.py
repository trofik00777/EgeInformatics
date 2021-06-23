from itertools import product


word = sorted(list("инставк"))
k = 0
for i in product(word, repeat=4):
    a = "".join(i)
    if a == "ника":
        print(k + 1)
    else:
        if a[0] in "нствк":
            if a[-1] in "иа":
                k += 1


