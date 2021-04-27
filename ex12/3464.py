def f(s):
    while "111" in s or "333" in s:
        if "333" in s:
            f3 = s.index("333")
            s = s[:f3] + "11" + s[f3 + 3:]

        if "111" in s:
            f1 = s.index("111")
            s = s[:f1] + "3" + s[f1 + 3:]


        print(s)

    if s:
        return int(s)
    else:
        return 0


f("1" * 100)
a = []
for i in range(100, 200):
    s = "1" * i
    a.append((f(s), -i))

print(a)
print(max(a))
