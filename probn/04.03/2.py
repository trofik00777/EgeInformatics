from itertools import permutations, product


def f(x, y, z, w):
    return (w and (x or z)) == (((1 - z) or y) and ((1 - y) or x))


data = [(1,1,1), (0,0,0), (1,0,1), (1,0,0)]
for i in permutations(data, r=4):
    a = [[i[k][j] for k in range(4)] for j in range(3)]
    if f(*a[0]) and f(*a[1]) and f(*a[2]):
        print(i)
