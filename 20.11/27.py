n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
a = [[max(i[0], i[1]), min(i[0], i[1]), abs(i[0] - i[1])] for i in a]
b = [i[0] for i in a]
sb = sum(b)
if sb % 3:
    print(sb)
else:
    c = [i[-1] for i in a if i[-1] % 3]
    c.sort()
    print(sb - c[0])
    # for i in [j for j in range(1, sb) if j % 3]:
    #     for k in a:
    #         if k[-1] == i:
    #             print(sb - i)
    #             exit()
