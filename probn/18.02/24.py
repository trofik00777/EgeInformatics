k = 0
maxk = 0
s = input()

for i in s:
    if i == ")":
        k += 1
    else:
        maxk = max(maxk, k)
        k = 0
maxk = max(maxk, k)
print(maxk)
