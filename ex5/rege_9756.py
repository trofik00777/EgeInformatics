for i in range(100, 1000):
    a = [(i // 100) * ((i // 10) % 10), ((i // 10) % 10) * (i % 10)]
    if min(a) == 6 and max(a) == 21:
        print(i)
        print(a)
        exit()
