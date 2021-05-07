with open("Задание 26/26.txt", "r") as f:
    a = f.read().strip().split("\n")

s, n = map(int, a[0].split())
data = [int(i) for i in a[1:]]
data.sort()
summ = 0
k = 0
last = None
for i in data:
    if summ + i > s:
        break
    summ += i
    k += 1
    last = i
delta = s - summ
maxn = last + delta
ns = [i for i in data if i <= maxn]
print(k, ns[-1])
