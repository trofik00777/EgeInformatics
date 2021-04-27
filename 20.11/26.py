size, n = map(int, input().split())
files = []
for i in range(n):
    files.append(int(input()))
files.sort()
for j in range(len(files), -1, -1):
    if sum(files[:j]) <= size:
        ost = size - sum(files[:j])
        d = [files[i] for i in range(j, len(files)) if files[j - 1] + ost >= files[i]]
        # if files[j - 1] + ost >= files[j]:
        #     answ = files[j]
        if d:
            answ = d[-1]
        else:
            answ = files[j - 1]
        print(j)
        print(answ)
        exit()
