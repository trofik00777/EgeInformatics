with open("datasets/27-62b.txt", "r") as f:
    a = f.read().strip().split("\n")

n = int(a[0])
nums = [int(i) for i in a[1:]]
nums.sort()

all_nums = set(nums)
answ = -1

for d in range(1, 101):
    data = [[i, True] for i in nums]

    for i in range(n):
        if not data[i][1]:
            continue

        start_ind = data[i][0]
        k = 0
        while start_ind in all_nums:
            k += 1
            start_ind += d
        answ = max(answ, k)

print(answ)
