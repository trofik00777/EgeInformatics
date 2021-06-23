n, s = map(int, input().split())

A, B = [], []
for i in range(n):
    a, b, mode = input().split()
    if mode == "A":
        A.append([int(a), int(b)])
    else:
        B.append([int(a), int(b)])

A.sort()
B.sort()

for i in B:
    for j in range(i[-1]):
        if s > i[0]:
            s -= i[0]

k = 0
for i in A:
    for j in range(i[-1]):
        if s > i[0]:
            s -= i[0]
            k += 1

print(k)
print(s)
