def f(x, y, z, w):
    return x and ((z and not w) or (y and not w) or (y and not z))


for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if f(x, y, z, w):
                    print(x, y, z, w)
