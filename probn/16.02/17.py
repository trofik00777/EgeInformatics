k = 0
m = 10000

for i in range(4855, 7857):
    if i % 8 == 0 and i % 19 == 0 and i % 7 and i % 16 and i % 24 and i % 26:
        k += 1
        m = min(m, i)
print(k, m)
