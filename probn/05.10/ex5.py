def alg(n: int):
    bin_n = bin(n)[2:]
    is1 = False
    k1, k2 = -1, -1
    for i in range(len(bin_n)):
        if bin_n[i] == "1" and not is1:
            is1 = True
            k1 = i
        # elif bin_n[i] == "0" and is1:
        #     k2 = i
        elif bin_n[i] == "1" and is1:
            k2 = i
            break
    new_n = bin_n[:k1] + bin_n[k2:]
    if new_n:
        return n - int(new_n, 2)
    return n


answ = []
for i in range(10, 1001):
    answ.append(alg(i))
print(set(answ))
print(answ)
