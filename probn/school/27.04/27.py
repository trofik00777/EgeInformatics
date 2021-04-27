mode = input()
if mode == "a":
    with open("27-54a.txt", "r") as f:
        a = f.read().split("\n")
    n = int(a[0])
    data = [int(i) for i in a[1:]]
    sums = []
    for i1 in range(n):
        for i2 in range(i1 + 1, n):
            for i3 in range(i2 + 1, n):
                for i4 in range(i3 + 1, n):
                    s = data[i1] + data[i2] + data[i3] + data[i4]

                    if s % 4 == 0:
                        sums.append(s)
    print(max(sums))
elif mode == "b":
    with open("27-54b.txt", "r") as f:
        a = f.read().split("\n")
    n = int(a[0])
    data = [int(i) for i in a[1:]]

    d = {i: [] for i in range(4)}
    data1 = []
    for i in data:
        d[i % 4].append(i)
    for i in range(4):
        d[i].sort(reverse=True)
        data1.extend(d[i][:4])

    sums = []
    n1 = len(data1)
    for i1 in range(n1):
        for i2 in range(i1 + 1, n1):
            for i3 in range(i2 + 1, n1):
                for i4 in range(i3 + 1, n1):
                    s = data1[i1] + data1[i2] + data1[i3] + data1[i4]

                    if s % 4 == 0:
                        sums.append(s)
    print(max(sums))
