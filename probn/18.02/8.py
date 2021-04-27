from itertools import permutations, product


d = set("нода")
gl = {"о", "а"}
sogl = {"н", "д"}
k = 0
for i in permutations(d, 4):
    # if i[0] in
    print("".join(i))
