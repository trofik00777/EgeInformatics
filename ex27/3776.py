n = int(input())

data = []
groups = {i: [] for i in range(10)}
for i in range(n):
    a = int(input())
    data.append(a)
    groups[a % 9].append(a)

data.sort()

data_perebor = []
for i in groups:
    groups[i].sort()
    groups[i] = groups[i][:4]
    data_perebor.extend(groups[i])
# print(groups)
# print(data_perebor)

summs = []
a = 0
n1 = len(data_perebor)

for i in range(n1):
    for j in range(i + 1, n1):
        for k in range(j + 1, n1):
            for r in range(k + 1, n1):
                s = data_perebor[i] + data_perebor[j] + data_perebor[k] + data_perebor[r]
                if s % 9 == 0:
                    summs.append(s)
# print(summs)
print(min(summs))
