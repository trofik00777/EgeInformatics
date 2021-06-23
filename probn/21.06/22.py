k = 0

for i in range(1, 6**4 + 1):
    x = i
    a = 0
    while x > 0:
        a = a + 1
        b = x % 6
        x = x // 6

    if a == 4 and b == 5:
        k += 1

print(k)
