with open("datasets/27-16b.txt", "r") as f:
    a = f.read().strip().split("\n")
# print(a[1:])

n = int(a[0])
data = [int(i) for i in a[1:]]

ind_13_1 = []
ind_13_2 = []
ind_all = set()

for i in range(n):
    if data[i] % 13 == 0:
        if (data[i] // 13) % 2 == 0:
            ind_13_2.append(i)
            ind_all.add(i)
        else:
            ind_13_1.append(i)
            ind_all.add(i)

# print()
# print(ind_13_1)
# print(ind_13_2)

max_n = max(max(ind_13_1), max(ind_13_2))
k = 0
f = []

k_1 = sum(1 for i in data if i % 2 != 0)
k_2 = n - k_1

for i in range(max_n + 1):
    a = data[i]
    if a % 13 == 0:
        if i in ind_13_1:
            k_1 -= 1
            c = k_2
            k += c
        else:
            k_2 -= 1
            c = k_1
            k += c
    else:
        if a % 2 == 0:
            c = sum(1 for j in ind_13_1 if j > i)
            k += c
            k_2 -= 1
        else:
            c = sum(1 for j in ind_13_2 if j > i)
            k += c
            k_1 -= 1
print(k)
