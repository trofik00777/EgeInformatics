des = ["0", "5"]
sot = [str(i) for i in range(2, 7)]

def check(n):
    s = str(n)
    if s[-2] not in des and s[-3] in sot:
        return True
    return False


k = []
for i in range(3905, 7999):
    if check(i):
        k.append(i)
print(k)
print(len(k))
print(min(k))
