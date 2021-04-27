s = input()

maxk = 0
k = 0
for i in s:
    if i == ")":
        k += 1
    else:
        maxk = max(maxk, k)
        k = 0
maxk = max(maxk, k)
print(maxk)
print(max(len(i) for i in s.split("(")))
