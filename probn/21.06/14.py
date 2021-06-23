def f(a, to):
    n = a
    s = "0123456789"
    answ = ""

    while n > 0:
        b = n % to
        n //= to
        answ += s[b]

    return answ[::-1]


print(f(9**20 + 3**60 - 5, 3).count("2"))
