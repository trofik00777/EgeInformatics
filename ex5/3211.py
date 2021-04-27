k = 0
for i in range(2, 1000):
    n = i
    bin_n = bin(n)[2:]
    bin_n += bin_n[-2]
    bin_n += bin_n[1]
    r = int(bin_n, 2)
    if 149 < r < 251:
        k += 1
print(k)
