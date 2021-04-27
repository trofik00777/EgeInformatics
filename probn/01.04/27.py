n = int(input())

h1, h2, h_a = 0, 0, 0
is_ch_nech = 0
diff = []

for _ in range(n):
    a, b, c = sorted(map(int, input().split()))
    h1 += a
    h2 += b
    h_a += c

    if (a + b) % 2:
        is_ch_nech += 1
    ac, bc = c - a, c - b
    k = []
    if ac % 2:
        k.append(ac)
    if bc % 2:
        k.append(bc)
    if k:
        diff.append(min(k))
diff.sort()

if h1 % 2 == 0 and h2 % 2 == 0:
    print("cool")
    print(h_a)
else:
    if (h1 + h2) % 2 == 0:
        if is_ch_nech > 1:
            print("chnch")
            print(h_a)
        else:
            print("not chnch")
            print(h_a - diff[0] - diff[1])
    else:
        print("bad")
