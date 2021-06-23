with open("24-173.txt", "r") as f:
    s = f.read().strip()

k = 0
max_k = -1
for i in range(len(s) - 5):
    s1 = s[i] + s[i + 1] + s[i + 2]
    s2 = s[i + 3] + s[i + 4] + s[i + 5]

    if s1 != s2:
        if k == 0:
            k = 6
        else:
            k += 1
    else:
        max_k = max(max_k, k)
        k = 0

print(max_k)
