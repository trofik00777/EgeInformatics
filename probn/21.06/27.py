with open("27-24b.txt", "r") as f:
    a = f.read().strip().split("\n")

n = int(a[0])
data = [map(int, i.split()) for i in a[1:]]
answ = [float("inf") for _ in range(10)]

for i in data[0]:
    answ[i % 10] = min(answ[i % 10], i)

for i in data[1:]:
    copy = [float("inf") for _ in range(10)]
    a, b = i

    for j in answ:
        if j < float("inf"):
            ab = [a + j, b + j]
            for k in ab:
                copy[k % 10] = min(copy[k % 10], k)

    answ = copy[:]

print(answ)
del answ[6]
print(min(answ))
