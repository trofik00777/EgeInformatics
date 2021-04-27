n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
data.sort()

k = 0
srar = float("inf")
for i in range(n - 1):
    n1 = data[i]
    for j in range(i + 1, min(i + 1 + 100 + 1, n)):
        if (n1 + data[j]) % 10 == 0:
            k += 1
            srar = min(srar, (n1 + data[j]) // 2)
print(k)
print(srar)


k = 0
srar = float("inf")
for i in range(n - 1):
    n1 = data[i]
    for j in range(i + 1, n):
        if (j - i <= 101) and (n1 + data[j]) % 10 == 0:
            k += 1
            srar = min(srar, (n1 + data[j]) // 2)
print(k)
print(srar)
