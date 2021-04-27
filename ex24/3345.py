with open("3345.txt", "r") as f:
    s = "B" + f.read() + "B"
print(s)
a = s.split("BOSS")
print(a)
k = [True for i in range(len(a) - 1)]

if a[0][-1] == "J":
    k[0] = False
for i in range(1, len(a)):
    if a[i]:
        if a[i][0] == "J":
            k[i - 1] = False
        if a[i][-1] == "J":
            k[i] = False
print(k.count(True))
