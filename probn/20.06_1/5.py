for i in range(501, 10000):
    n = i
    bin_n = bin(n)[2:][::-1]

    r = int(bin_n, 2)
    if r == 19:
        print(i)
        break
