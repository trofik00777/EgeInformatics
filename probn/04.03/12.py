def f(a):
    s = a
    while "111" in s:
        ind = s.index("111")
        s = s[:ind] + "2" + s[ind + 3:]
        if "222" in s:
            ind = s.index("222")
            s = s[:ind] + "1" + s[ind + 3:]
    return s


for i in range(36, 100):
    s = "1" * i

    a = f(s)
    if a == "1":
        print(i)
        exit()
