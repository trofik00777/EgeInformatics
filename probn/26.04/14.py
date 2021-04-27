def f(a, to):
    n = a
    s = "0123456789"
    k = ""
    while n > 0:
        b = n % to
        k += s[b]
        n //= to

    return k[::-1]


print(f((512**78 - 512**60)*(512**5 + 64**5), 8).count("7"))
