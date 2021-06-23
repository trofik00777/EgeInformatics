with open("27-9b.txt", "r") as f:
    a = f.read().strip().split("\n")

n = int(a[0])
data = [int(i) for i in a[1:]]
answ = float("inf")

nch = [(data[i], i) for i in range(n) if data[i] % 2 != 0]
nch.sort()

print(nch)
