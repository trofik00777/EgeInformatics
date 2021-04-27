s = input()

k = 1
maxk = 0
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        k += 1
    else:
        maxk = max(maxk, k)
        k = 1
maxk = max(maxk, k)
print(maxk)
