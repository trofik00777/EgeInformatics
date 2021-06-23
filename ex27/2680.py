with open("datasets/27-20b.txt", "r") as f:
    a = f.read().strip().split("\n")

n = int(a[0])
dominos = [tuple(i.split()) for i in a[1:]]

maybe_link = []
for i in range(1, n):
    a, b = dominos[i - 1]

    if a in dominos[i] or b in dominos[i]:
        maybe_link.append(1)
    else:
        maybe_link.append(0)

print(maybe_link)

len_cep = 1
max_len = -1
last_point = (set(dominos[0])&set(dominos[1])).pop()

for i in range(1, n):
    if maybe_link[i - 1] == 1:
        if len_cep == 1:
            last_point = (set(dominos[i - 1])&set(dominos[i])).pop()
            len_cep += 1
        else:
            if len(set(dominos[i - 1])) == 1:
                must = dominos[i - 1][0]
            else:
                must = (set(dominos[i - 1]) - set(last_point)).pop()
            if must in dominos[i]:
                len_cep += 1
                last_point = must
            else:
                max_len = max(max_len, len_cep)
                len_cep = 1
    else:
        max_len = max(max_len, len_cep)
        len_cep = 1

print(max_len)
