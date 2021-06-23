def f(a, to):
    n = a
    s = "0123456789"
    k = ""
    while n > 0:
        b = n % to
        k += s[b]
        n //= to
    return k[::-1]


print(f(36**17 + 6**66 - 216, 6).count("5"))
