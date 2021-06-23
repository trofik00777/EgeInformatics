with open("27-31b.txt", "r") as f:
    s = f.read().strip().split("\n")

n = int(s[0])
answ = 0
d = []
for i in s[1:]:
    a, b, c = sorted(map(int, i.split()))

    answ += a + b
    da, db = c - a, c - b
    if da % 9:
        d.append(da)
    if db % 9:
        d.append(db)

if answ % 9:
    print(answ)
else:
    print(answ + min(d))
