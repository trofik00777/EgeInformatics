with open("Задание 27/27_B.txt", "r") as f:
    a = f.read().strip().split("\n")

n = int(a[0])
data = []
s = 0
answ = [-1 for _ in range(109)]
a1, b, c = sorted(map(int, a[1].split()))
answ[a1 % 109] = a1
answ[b % 109] = max(answ[b % 109], b)
answ[c % 109] = max(answ[c % 109], c)

for i in a[2:]:
    a, b, c = sorted(map(int, i.split()))
    data.append((a, b, c))

    copy = [-1 for _ in range(109)]
    for j in answ:
        if j > -1:
            aj, bj, cj = a + j, b + j, c + j

            copy[aj % 109] = max(copy[aj % 109], aj)
            copy[bj % 109] = max(copy[bj % 109], bj)
            copy[cj % 109] = max(copy[cj % 109], cj)
    answ = copy[:]
print(answ)
print(max(answ[1:]))
