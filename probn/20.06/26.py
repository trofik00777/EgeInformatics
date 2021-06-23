with open("26-j2.txt", "r") as f:
    a = f.read().strip().split("\n")

n = int(a[0])
data = [int(i) for i in a[1:]]

data.sort()
mediane = data[500000]
avrg = sum(data) / len(data)
k = 0

for i in data:
    if avrg <= i <= mediane:
        k += 1

print(k)
