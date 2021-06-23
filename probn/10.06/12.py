s = "1" * 99

while "111" in s:
    s = s.replace("111", "22", 1)
    if "222" in s:
        s = s.replace("222", "11", 1)
print(s)
