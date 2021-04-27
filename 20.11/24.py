with open("24.txt", "r") as f:
    s = f.read().strip()

k = 0
answ_k = 0
pred = ""
for i in s:
    if i != pred:
        k += 1
        pred = i
    else:
        answ_k = max(answ_k, k)
        k = 1
        pred = i

print(answ_k)
