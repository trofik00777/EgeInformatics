def check(x, y, to):
    n = x
    s = "0123456789"
    k = ""
    while n > 0:
        b = n % to
        k += s[b]
        n //= to
    a = int(k[::-1])
    if k == "":
        a = 0
    print(a)
    return a + y == 10


k = []
for i in range(100001, 900009 + 1):
    if i % 11 == 0 and i % 55:
        if i % 7 + i % 10 == 10:
            k.append(i)

print(k)
print(max(k))
print(len(k))
