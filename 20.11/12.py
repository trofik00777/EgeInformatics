s = "8" * 70
while "2222" in s or "8888" in s:
    if "2222" in s:
        ind = s.index("2222")
        s = s[:ind] + "88" + s[ind + 4:]
    else:
        ind = s.index("8888")
        s = s[:ind] + "22" + s[ind + 4:]
print(s)
