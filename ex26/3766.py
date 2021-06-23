def check(s):
    less, big = 0, 0
    for i in range(n):
        if s > data[i]:
            less += 1
        if s < data[i]:
            big += 1
    return 2 * less >= n and 4 * big >= n


n = int(input())
data = [int(input()) for i in range(n)]
data.sort()

pairs = []
for i in range(n):
    for j in range(i + 1, n):
        s = data[i] + data[j]
        if s % 2 == 0:
            if 2 * data[n // 2 - 1] < s < 2 * data[-(n // 4)]:
                pairs.append((data[i], data[j], s // 2))
            # if check(s // 2):
            #     pairs.append((data[i], data[j], s // 2))

print(pairs)
print(len(pairs))
print(min(pairs, key=lambda x: x[-1]))
