a = [[int(j) for j in i.split()] for i in """51	21	93	48	45	100	67	39	18	29
57	43	97	51	92	10	93	32	19	58
63	16	31	16	78	88	90	72	37	67
10	57	64	25	96	50	81	65	91	69
99	43	95	7	40	76	18	34	5	65
35	19	71	77	64	38	62	56	10	2
100	57	27	26	51	33	100	11	53	1
11	79	49	46	37	69	80	31	25	39
22	71	20	23	11	12	39	16	64	34
4	25	87	84	30	48	77	13	40	33
""".split("\n")][:-1]
print(a)
gr = len(a)
answ_min = 1000000000000000000000
answ_max = 0


def f(x, y, n):
    print(x, y)
    s = n + a[x][y]
    if x + 1 >= gr and y + 1 >= gr:
        global answ_max
        global answ_min
        print(a[x][y])
        if s > answ_max:
            answ_max = s
        if s < answ_min:
            answ_min = s
    else:
        if x + 1 < gr:
            f(x + 1, y, s)
        if y + 1 < gr:
            f(x, y + 1, s)


print(gr)
f(0, 0, 0)
print(answ_max, answ_min)
