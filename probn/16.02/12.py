s = "9" * 1000

while "999" in s or "888" in s:
    if "888" in s:
        ind = s.index("888")
        s = s[:ind] + "9" + s[ind + 3:]
    else:
        ind = s.index("999")
        s = s[:ind] + "8" + s[ind + 3:]
print(s)
