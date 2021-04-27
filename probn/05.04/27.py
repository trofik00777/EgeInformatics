n = int(input())

data = []
for i in range(n):
    a, b = sorted(map(int, input().split()))
    data.append((a, b))

answ = [float("inf") for i in range(8)]
answ[data[0][0] % 8] = data[0][0]
answ[data[0][1] % 8] = min(answ[data[0][1] % 8], data[0][1])

del data[0]

for a, b in data:
    copy = [float("inf") for j in answ]
    for i in answ:
        if i < float("inf"):
            n1, n2 = a + i, b + i
            copy[n1 % 8] = min(copy[n1 % 8], n1)
            copy[n2 % 8] = min(copy[n2 % 8], n2)
    answ = copy[:]

print(answ)

del answ[2]
print(min(answ))
