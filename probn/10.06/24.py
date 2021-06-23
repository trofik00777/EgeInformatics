answ = dict()

with open("24-s2.txt", "r") as f:
    s = f.read().strip()

for i in range(len(s) - 2):
    if s[i] == "X" and s[i + 2] == "Z":
        a = s[i + 1]
        if a in answ:
            answ[a] += 1
        else:
            answ[a] = 1



max_s = ""
max_k = 0
for i in sorted(list(answ.keys())):
    c = answ[i]
    if c > max_k:
        max_k = c
        max_s = i
print(max_s, max_k)
