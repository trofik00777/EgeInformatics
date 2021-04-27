for i in range(256):
    n = i
    bin_n = bin(n)[2:]
    b_n = "0" * (8 - len(bin_n)) + bin_n
    r = int("".join([str(1 - int(j)) for j in b_n]), 2)
    if r == 204:
        print(i + 1)
