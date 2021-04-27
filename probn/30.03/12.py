def algor(a):
    s = a
    while "111" in s:
        ind = s.index("111")
        s = s[:ind] + "2" + s[ind + 3:]
        if "2222" in s:
            ind = s.index("2222")
            s = s[:ind] + "333" + s[ind + 4:]
        if "33" in s:
            ind = s.index("33")
            s = s[:ind] + "1" + s[ind + 2:]
    return s.count("1")


k = dict()
for i in range(91, 2000):
    a = "1" * i
    b = algor(a)
    if b in k:
        pass
    else:
        k[b] = i
print(k[max(k.keys())])
print(max(k.keys()))
