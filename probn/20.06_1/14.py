def f(a, to):
    n = a
    s = "0123456789"
    answ = ""

    while n > 0:
        b = n % to
        n //= to
        answ += s[b]

    return answ[::-1]


print(sum(int(i) for i in f(9**7 + 3**21 - 8, 3)))
