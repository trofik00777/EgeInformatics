n = int(input())
a, b = map(int, input().split())

data = [float("inf") for _ in range(16)]
data[a % 16] = a
data[b % 16] = min(data[b % 16], b)

for i in range(n - 1):
    a, b = map(int, input().split())

    copy = [float("inf") for _ in range(16)]

    for j in data:
        if j < float("inf"):
            a1, b1 = j + a, j + b

            copy[a1 % 16] = min(copy[a1 % 16], a1)
            copy[b1 % 16] = min(copy[b1 % 16], b1)
    data = copy[:]

print(data)
print(data[15])
