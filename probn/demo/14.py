def f(a, to):
    n = a
    s = "0123456789"
    k = ""
    while n > 1:
        b = n % to
        k += s[b]
        n //= to
    return k[::-1]


print(f(7*(512**120) - 6 * (64**100) + 8**210 - 255, 8).count("0"))
