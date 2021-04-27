def f(a, to):
    n = a
    s = "0123456789"
    answ = ""
    while n > 0:
        b = n % to
        answ += s[b]
        n //= to
    return answ[::-1]


print(f(67, 3))
