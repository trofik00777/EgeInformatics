with open("27-b.txt", "r") as f:
    af = f.read().strip().split("\n")

n = int(af[0])
data = [0 for _ in range(3)]

a, b = map(int, af[1].split())
data[a % 3] = a
data[b % 3] = max(data[b % 3], b)

for i in af[2:]:
    a, b = map(int, i.split())

    copy = [0 for _ in range(3)]
    for j in data:
        if j > 0:
            ab = [a + j, b + j]
            for k in ab:
                copy[k % 3] = max(copy[k % 3], k)

    data = copy[:]

print(data)
print(max(data[1:]))


