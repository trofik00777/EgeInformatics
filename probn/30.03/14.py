def f(a, to):
    s = "0123456789"
    n = ""
    while a > 0:
        b = a % to
        a //= to
        n += s[b]
    return n[::-1]


print(f(128**30 + 16**60 - 16, 8).count("7"))
