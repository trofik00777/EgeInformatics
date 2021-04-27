n = int(input())

data = []

for _ in range(n):
    data.append(int(input()))
data.sort()

k = len(data) // 10
# data = data[k:]
# data = data[:len(data) - k]
data = data[k:len(data) - k]
print(sum(data))
print(max(data))
