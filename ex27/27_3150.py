with open("datasets/27-44a.txt", "r") as f:
    inp_data = f.read().split("\n")
n = int(inp_data[0])
inp_data = inp_data[1:]

heap_answ = 0
heap_1 = 0
heap_2 = 0
# min_diff = 0
min_diff = []
flag_ch_nech = False

for three in inp_data:
    a, b, c = sorted(map(int, three.split()))
    heap_answ += c
    heap_1 += a
    heap_2 += b

    if (a + b) % 2 != 0:
        flag_ch_nech = True

    cond = min(c - a, c - b)
    # if cond % 2 != 0 and cond < min_diff:
    #     min_diff = cond
    if cond % 2 != 0:
        min_diff.append(cond)
min_diff.sort()

# --------------------------------------- debug print
print(heap_answ, heap_1, heap_2)
print(min_diff[:5])
print()
# --------------------------------------- debug print

if heap_1 % 2 != 0 and heap_2 % 2 != 0:
    print(heap_answ)
    exit()
elif (heap_1 + heap_2) % 2 != 0:
    print(heap_answ - min_diff[0])
    exit()
else:
    if flag_ch_nech:
        print(heap_answ)
        exit()
    else:
        print(heap_answ - min_diff[0] - min_diff[1])
