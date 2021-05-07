with open("Задание 27/27_B.txt", "r") as f:
    a = f.read().strip().split("\n")

n = int(a[0])
data = []
s = 0
deltas = []

for i in a[1:]:
    a, b, c = sorted(map(int, i.split()))
    data.append((a, b, c))

    s += c
    dac, dbc = c - a, c - b
    if dac % 109:
        deltas.append(dac)
    if dbc % 109:
        deltas.append(dbc)
if s % 109:
    print(s)
else:
    print(s - min(deltas))
