s = "1" * 198

while "1111" in s:
    ind = s.index("1111")
    s = s[:ind] + "33" + s[ind + 4:]
    if "333" in s:
        ind1 = s.index("333")
        s = s[:ind1] + "1" + s[ind1 + 3:]
print(s)
