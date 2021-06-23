def f(a, b, c):
    return (a and b) or (c and (not a or b))


for b in 0, 1:
    for c in 0, 1:
        for a in 0, 1:
            print(b, c, a, int(f(a, b, c)))
