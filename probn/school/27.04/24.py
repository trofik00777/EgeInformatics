with open("24-s1.txt", "r") as f:
    data = f.read().strip().lower().split("\n")


maxk = 0
maxi = 0
for i in range(len(data)):
    k = data[i].count("q")
    if k >= maxk:
        maxk = k
        maxi = i

s = data[maxi]
letters = list(set(s))
letters.sort()
minl = float("inf")
minn = ""
for i in letters:
    l_let = s.count(i)
    if l_let < minl:
        minl = l_let
        minn = i
print(minn, "".join(data).count(minn))
