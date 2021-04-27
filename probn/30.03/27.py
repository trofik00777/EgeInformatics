n = int(input())
data_umensh = []
s = 0
for i in range(n):
    a, b, c = sorted(map(int, input().split()), key=lambda x: -x)
    s += a + b
    ac, bc = a - c, b - c
    if ac % 5:
        data_umensh.append(ac)
    if bc % 5:
        data_umensh.append(bc)

if s % 5 == 0:
    print(s - min(data_umensh))
else:
    print(s)
