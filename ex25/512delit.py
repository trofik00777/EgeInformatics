from itertools import product


a = set("12345")
b = set()
for i in product(a, repeat=len(a)):
    # print(i)
    j = "".join(sorted(list(i)))
    b.add(j)

for i in sorted(list(b)):
    print(i)
print(len(b))
