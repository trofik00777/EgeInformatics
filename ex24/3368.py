with open("3368.txt", "r") as f:
    s = f.read()
print(s)
max_up = 0
k = 1
for i in range(1, len(s)):
    if ord(s[i]) > ord(s[i - 1]):
        k += 1
    else:
        max_up = max(max_up, k)
        k = 1
print(max_up)
