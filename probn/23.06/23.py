A = []



def f(n, k):
    global A
    if k == 15:
        A.append(n)
        return

    f(n * 2, k + 1)
    f(n * 2 + 1, k + 1)


f(1, 0)
print(len(set(A)))






