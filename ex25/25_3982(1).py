def f(a):
    numb = a
    n = m = 0
    while numb % 14 == 0:
        n += 1
        m += 1
        numb //= 14
    if numb % 2 == 0:
        if m % 2 == 0:
            while numb % 2 == 0:
                n += 1
                numb //= 2
            if numb == 1 and n % 2 != 0:
                return True
        return False
    elif numb % 7 == 0:
        if n % 2 != 0:
            while numb % 7 == 0:
                m += 1
                numb //= 7
            if numb == 1 and m % 2 == 0:
                return True
        return False
    return False
    # while numb % 2 == 0 or numb % 7 == 0:
    #     if numb % 2 == 0:
    #         n += 1
    #         numb //= 2
    #     if numb % 7 == 0:
    #         m += 1
    #         numb //= 7
    #
    # if n > 1:
    #     return False
    #
    # if n % 2 != 0 and n % 2 == 0:
    #     return True
    # return False


for i in range(100000000, 300000000 + 1):
    # if i % 1000 == 0:
    #     print(i)
    if f(i):
        print(i)
