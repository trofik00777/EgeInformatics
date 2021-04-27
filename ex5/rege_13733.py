for i in range(1, 1000):
    n = i
    bin_n = bin(n)[2:]
    k = bin_n.count("1")
    bin_n = bin_n + str(k % 2) + "0"
    r = int(bin_n, 2)

    if r > 83:
        print(r)
        exit()
