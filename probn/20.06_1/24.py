with open("24-1.txt", "r") as f:
    s = f.read().strip()

k = 1
max_k = -1
posl = ""

for i in range(1, len(s)):
    if s[i] < s[i - 1]:
        k += 1
    else:
        if max_k < k:
            posl = s[i - k + 1:i + 1]
        max_k = max(max_k, k)
        k = 1

print(max_k)
print(posl)
