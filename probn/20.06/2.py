def f(x, y, z, w):
    return (x and z) or ((not w or x) == (not z or y))


for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = f(x, y, z, w)
                if not F:
                    print(x, y, z, w)
