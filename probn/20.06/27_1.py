with open("27-31a.txt", "r") as f:
    s = f.read().strip().split("\n")

n = int(s[0])
answ = 0
d = []

data = [float("inf") for i in range(9)]
a, b, c = sorted(map(int, s[1].split()))
ab, ac, bc = a + b, a + c, b + c
data[ab % 9] = ab
data[ac % 9] = min(data[ac % 9], ac)
data[bc % 9] = min(data[bc % 9], bc)


for i in s[2:]:
    a, b, c = sorted(map(int, i.split()))

    copy = [float("inf") for i in range(9)]
    for j in data:
        if j < float("inf"):
            abacbc = [a + b + j, a + c + j, b + c + j]

            for k in abacbc:
                copy[k % 9] = min(copy[k % 9], k)
    data = copy[:]

print(data)
print(min(data[1:]))
