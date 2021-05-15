for i in range(1, 1000):
    n = i
    bin_n = bin(n)[2:]
    bin_n += bin_n[-1]
    bin_n += str(bin_n.count("1") % 2)
    bin_n += str(bin_n.count("1") % 2)

    r = int(bin_n, 2)
    if r > 136:
        print(i)
        break
