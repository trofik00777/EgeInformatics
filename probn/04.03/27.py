n = int(input())

data = [float("inf") for i in range(10)]
for i in range(n):
    if len(set(data)) == 1:
        a, b = map(int, input().split())
        data[a % 10] = a
        data[b % 10] = min(data[b % 10], b)
        continue

    copy = [float("inf") for j in range(10)]
    a, b = map(int, input().split())
    for j in data:
        if j < float("inf"):
            a1, b1 = j + a, j + b
            copy[a1 % 10] = min(copy[a1 % 10], a1)
            copy[b1 % 10] = min(copy[b1 % 10], b1)
    data = copy[:]
print(data)
print(data[4])
