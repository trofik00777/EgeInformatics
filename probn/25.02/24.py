with open("24-s1.txt", "r") as f:
    data = f.read().split("\n")

print(data)
print(len(data))
k = 0
for i in data:
    if i.count("K") > i.count("U"):
        k += 1
print(k)
