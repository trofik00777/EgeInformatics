prost = [i for i in range(2, 10001000)]

n = len(prost)
for i in range(n):
    if prost[i] != 0:
        for j in range(i + prost[i], n, prost[i]):
            prost[j] = 0
prost = [i for i in prost if i > 0]
print(prost[-100:])
