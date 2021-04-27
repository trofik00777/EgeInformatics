def check(a):
    for y in range(1, 100):
        for x in range(1, 100):
            if not ((x**2 - 3*x + 2 > 0) or (y > x**2+7) or (x*y < a)):
                return False
    return True


for a in range(1000):
    if check(a):
        print(a)
        break
