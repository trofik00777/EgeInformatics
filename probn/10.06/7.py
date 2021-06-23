from itertools import product


d = set("жалей")
k = 0
for i in product(d, repeat=5):
    if i.count("й") < 2:
        if i.count("й") == 0:
            k += 1
            print(i)
        else:
            ind = i.index("й")
            if ind == 0 or ind == 4:
                continue
            else:
                if i[ind - 1] != "е" and i[ind + 1] != "е":
                    k += 1
                    print(i)
print(k)
