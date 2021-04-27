s = "8" * 9 + "5" * 12

while "555" in s or "888" in s:
    while "555" in s:
        ind = s.index("555")
        s = s[:ind] + "8" + s[ind + 3:]
    while "888" in s:
        ind = s.index("888")
        s = s[:ind] + "5" + s[ind + 3:]

print(s)
