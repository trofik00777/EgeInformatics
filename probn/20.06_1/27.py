with open("27-9b.txt", "r") as f:
    a = f.read().strip().split("\n")

n = int(a[0])
data = [int(i) for i in a[1:]]
answ = float("inf")

for i in range(n):
    a = data[i]
    if a % 2 == 0:
        continue

    for j in range(i + 6, n):
        b = data[j]
        if b % 2 == 0:
            continue

        answ = min(answ, a * b)

print(answ)
