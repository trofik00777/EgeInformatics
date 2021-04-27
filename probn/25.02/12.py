s = "1" * 2018 + "3" * 2050

while "111" in s:
    ind = s.index("111")
    s = s[:ind] + "2" + s[ind + 3:]
    if "222" in s:
        ind = s.index("222")
        s = s[:ind] + "3" + s[ind + 3:]
    if "333" in s:
        ind = s.index("333")
        s = s[:ind] + "1" + s[ind + 3:]
print(s)
