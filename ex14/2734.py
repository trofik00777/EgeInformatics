for x in range(4, 100):
    print(sum(int(i) for i in oct((88 + 2 * (8**x)) * (8**x) + 88 + 8**8)[2:]))
