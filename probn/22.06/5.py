for i in range(1, 256):
    n = i
    bin_n = bin(n)[2:]

    bin_n = "0" * (8 - len(bin_n)) + bin_n
    bin_n_rev = "".join("0" if i == "1" else "1" for i in bin_n)

    r = int(bin_n_rev, 2)
    if r - i == -21:
        print(i)
