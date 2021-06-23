def f(x, y, z, w):
    return (w and y) or ((not x or w) == (not y or z))


for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if not f(x, y, z, w):
                    print(x, y, z, w)
