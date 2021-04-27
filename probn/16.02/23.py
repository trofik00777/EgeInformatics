fibo = [0 for _ in range(21)]
fibo[3] = 1

lf = len(fibo)
for i in range(lf):
    a = i + 1
    b = i + 2
    if a < lf:
        fibo[a] += fibo[i]
    if b < lf:
        fibo[b] += fibo[i]
print(fibo)
k = fibo[9]
print(fibo[9])

fibo = [0 for _ in range(21)]
fibo[9] = k

lf = len(fibo)
for i in range(lf):
    a = i + 1
    b = i + 2
    if a < lf and a != 15:
        fibo[a] += fibo[i]
    if b < lf and b != 15:
        fibo[b] += fibo[i]
print(fibo)
k = fibo[9]
print(fibo[20])
