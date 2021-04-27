with open("3157.txt", "r") as f:
    s = f.read().lower()
print(s)
counts = {}
for i in range(len(s) - 2):
    if s[i] == "x":
        if s[i + 2] == "z":
            a = s[i + 1]
            if a in counts:
                counts[a] += 1
            else:
                counts[a] = 1
print([i for i in counts if counts[i] == max(counts.values())])
