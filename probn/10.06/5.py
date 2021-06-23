for i in range(1000, 0, -1):
    n = i
    bin_n = bin(n)[2:]
    bin_n += str(bin_n.count("1") % 2)
    bin_n += "0"

    r = int(bin_n, 2)
    if r < 50:
        print(r)
        break
