with open("27-41b.txt", "r") as f:
    a = f.read().strip().split("\n")

n = int(a[0])
h1, h2, h_answ = 0, 0, 0
is_ch_nch = False
deltas = []

for i in a[1:]:
    a, b, c = sorted(map(int, i.split()))

    h_answ += a
    h1 += b
    h2 += c

    if (b + c) % 2 != 0:
        is_ch_nch = True

    db, dc = b - a, c - a

    if db % 2 != 0:
        deltas.append(db)
    if dc % 2 != 0:
        deltas.append(dc)

if (h1 + h2) % 2 != 0:
    print(h_answ, is_ch_nch)
else:
    print(h_answ + min(deltas))


