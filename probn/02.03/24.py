s = input()

digs = set("1234567890")
k = []
curr = ""
for i in s:
    if i in digs:
        curr += i
    else:
        if curr:
            a = int(curr)
            if a % 2 == 0:
                k.append(a)
            curr = ""
print(k)
print(min(k))
