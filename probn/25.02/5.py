for i in range(1, 1000):
    n = i
    bin_n = bin(n)[2:]
    if n % 2:
        bin_n = bin_n + "10"
    else:
        bin_n = bin_n + "01"

    r = int(bin_n, 2)
    if r > 81:
        print(r)
        exit()
