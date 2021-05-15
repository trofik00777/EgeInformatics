from itertools import permutations


k = []
for i in permutations(list("кабала"), r=6):
    fl = True
    if all(i[j - 1] != i[j] for j in range(1, 6)):
        k.append("".join(i))
    else:
        print("".join(i))
print(len(set(k)))
a = ["", '"']
