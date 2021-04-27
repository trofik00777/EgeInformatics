n = int(input())
data = []
for i in range(n):
    data.append(int(input()) % 14)

k = 0
for i in range(n):
    must = 14 - data[i]
    k += data[i + 5:].count(must)
print(k)
