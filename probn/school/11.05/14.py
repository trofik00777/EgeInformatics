def f(a):
    n = a
    s = "0123456789"
    k = ""

    while n > 0:
        b = n % 3
        n //= 3
        k += s[b]

    return k[::-1]


print(f(9**7 + 3**21 - 9).count("0"))
