with open("k7a-6.txt", "r") as f:
    s = f.read().strip()

k = 0
max_k = -1

for i in range(len(s)):
    if s[i] not in "AE":
        k += 1
    else:
        max_k = max(max_k, k)
        k = 0

print(max_k)
