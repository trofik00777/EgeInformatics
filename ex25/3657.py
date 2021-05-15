def check(a: str):
    if max(a) < "3":
        if sum(map(int, a)) % 10 == 0:
            return True
    return False


print(check("1212121"))

answ = []
for i in range(1000000, 1300000 + 1):
    if check(str(i)):
        answ.append(i)

print(answ[9::10])
