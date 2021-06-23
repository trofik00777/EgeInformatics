def f(a):
    i = 2
    while i * i <= a:
        if a % i == 0:
            return False

        i += 1

    return True


k = []
for i in range(3000001, 10000000, 2):
    if f(i):
        k.append(i)
        print(i)

print(k)
