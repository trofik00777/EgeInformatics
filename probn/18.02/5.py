for i in range(1000):
    n = i
    bin_n = bin(n)[2:]
    bin_n = bin_n + bin_n[-1]
    s = bin_n.count("1")
    bin_n = bin_n + str(s % 2) + "0"

    r = int(bin_n, 2)
    if r > 114:
        print(r)
        exit()
