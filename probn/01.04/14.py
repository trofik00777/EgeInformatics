def f(a, to):
    n = a
    s = "0123456789"
    k = ""
    while n > 0:
        b = n % to
        n //= to
        k += s[b]
    return k[::-1]


print(f(4, 3))
a = f(9**5 + 3**25 - 20, 3)
k = sum(int(i) for i in a)
print(k)
