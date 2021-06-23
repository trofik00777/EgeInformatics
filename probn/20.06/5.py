for i in range(1000):
    n = i
    bin_n = bin(n)[2:]

    bin_n += str(bin_n.count("1") % 2) + "0"

    r = int(bin_n, 2)
    if r > 108:
        print(r)

