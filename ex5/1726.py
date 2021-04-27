for i in range(100, 1000):
    n = i
    a = [int(j) for j in str(n)]
    a.sort()
    max_n = a[-1] * 10 + a[1]
    if a[0]:
        min_n = a[0] * 10 + a[1]
    else:
        min_n = a[1] * 10 + a[0]
    d = max_n - min_n
    if d == 60:
        print(i)
        exit()
