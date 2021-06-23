with open("datasets/27986_B.txt", "r") as f:
    data = [int(i) for i in f.read().strip().split("\n")[:-1]]


max_div_7 = 0
max_numb = 0

for i in data:
    if i % 7 == 0 and i % 49 != 0:
        max_div_7 = max(max_div_7, i)
    else:
        max_numb = max(max_numb, i)

if max_div_7 * max_numb == 0:
    print(1)
else:
    print(max_div_7 * max_numb)



