n = int(input())

data = []
for i in range(n):
    a = list(sorted(map(int, input().split())))
    a.append(min(a[-1] - a[0], a[-2] - a[0]))
    data.append(a)
print(data)

s = sum(i[-2] + i[-3] for i in data)
if s % 5:
    print(s)
    exit()
else:
    s -= min([i[-1] for i in data if i[-1] % 5])
    print(s)
    exit()
