k = 0

for i in range(100000):
    x = i
    a = 0
    b = 1
    while x > 0:
        a = a + 1
        if x % 14 != 0:
            b = b * (x % 14)
        x = x // 14

    if a == 2 and b == 12:
        k += 1


print(k)


