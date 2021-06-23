k = []
a = 1
while a <= 5000:
    b = a
    while b <= 5000:
        c2 = a ** 2 + b ** 2
        if c2 <= 25000000 and int(c2 ** .5) == c2 ** .5:
            k.append([a, b, int(c2 ** .5)])

        b += 1

    a += 1

print(k)
print(len(k))
print(max([(sum(i), i[-1]) for i in k]))
