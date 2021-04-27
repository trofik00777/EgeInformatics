k = 0
maxk = 0
gl = {"A", "E"}

s = input()
for i in s:
    if i in gl:
        maxk = max(maxk, k)
        k = 0
    else:
        k += 1
print(maxk)
