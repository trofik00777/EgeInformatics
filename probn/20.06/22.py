k = 0

for i in range(1000000):
    x = i
    a = 0
    b = 1
    while x > 0:
        a = a + 1
        if x % 8 != 0:
            b = b * (x % 8)
        x = x // 8

    if a == 3 and b == 24:
        k += 1

print(k)
