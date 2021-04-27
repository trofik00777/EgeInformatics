n = int(input())
data = [float("inf") for i in range(16)]
for i in range(n):
    a, b = map(int, input().split())
    if len(set(data)) == 1:
        data[a % 16] = a
        data[b % 16] = min(data[b % 16], b)
        print(1)
        continue

    copy = [float("inf") for j in range(16)]
    for j in data:
        if j < float("inf"):
            a1, b1 = a + j, b + j
            copy[a1 % 16] = min(copy[a1 % 16], a1)
            copy[b1 % 16] = min(copy[b1 % 16], b1)
    data = copy[:]

print(data)
print(data[15])
