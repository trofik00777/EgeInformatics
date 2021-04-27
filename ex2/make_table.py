def f(a, b, c, d):
    return ((not (not b or a)) and (not c or d)) != (a and b and c and not d)



a = [0, 1]
for x in a:
    for y in a:
        for z in a:
            for w in a:
                res_f = f(x, y, z, w)
                if res_f:
                    print(x, y, z, w)
