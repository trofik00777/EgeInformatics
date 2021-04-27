for i in range(1000):
    n = i
    bin_n = bin(n)[2:]
    if n % 2 == 0:
        bin_n = "1" + bin_n
    else:
        bin_n += "0"
    k = bin_n.count("1")
    if k % 2 == 0:
        bin_n += "1"
    else:
        bin_n += "0"

    r = int(bin_n, 2)
    print(f"{i}:\t{r}")
    if r > 228:
        print(i)
        exit()
