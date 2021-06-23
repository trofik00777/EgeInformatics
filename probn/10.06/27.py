with open("27-45b.txt", "r") as f:
    a = f.read().strip().split("\n")

n = int(a[0])
h1, h2, h_answ = 0, 0, 0
ch_nch = False
deltas = []

for i in a[1:]:
    a, b, c = sorted(map(int, i.split()))

    h_answ += a
    h1 += b
    h2 += c
    if (b + c) % 2:
        ch_nch = True
    db, dc = b - a, c - a
    if db % 2 and dc % 2:
        deltas.append(min(db, dc))
    elif db % 2:
        deltas.append(db)
    elif dc % 2:
        deltas.append(dc)

deltas.sort()
print(deltas)
if h1 % 2 and h2 % 2:
    print(h_answ)
    print(1)
else:
    if (h1 + h2) % 2 == 0:
        if ch_nch:
            print(h_answ)
            print(2)
        else:
            print(h_answ + deltas[0] + deltas[1])
            print(3)
    else:
        print(h_answ + deltas[0])
        print(4)
# 1239 151970679
