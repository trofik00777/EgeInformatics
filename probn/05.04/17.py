def check(n):
    s = str(n)
    a = [int(i) for i in s]
    return ("1" not in s) and (max(a) - min(a) < 4)


k = []
for i in range(1005, 147870 + 1):
    a = check(i)
    if a:
        k.append(i)
k = k[::-1]
print(len(k))
print(k[24])
