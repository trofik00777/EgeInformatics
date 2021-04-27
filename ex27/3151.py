n = int(input())
nums = []
for _ in range(n):
    nums.append(list(sorted(map(int, input().split()))))
nums = [[
    [i[0], i[1], i[-1]], [i[-1] - i[0], i[1] - i[0]]
] for i in nums]
k3 = []
k1 = [i[0][-1] for i in nums]
k2 = [i[0][1] for i in nums]
sum1 = sum(k1)
sum2 = sum(k2)
sum3 = sum([i[0][0] for i in nums])
if sum1 % 2 and sum2 % 2:
    print(sum3)
    exit()
else:
    if any([sum1 % 2, sum2 % 2]):
        if sum1 % 2:
            sum_ch = sum2
            sum_nch = sum1
        else:
            sum_ch = sum1
            sum_nch = sum2
        nums_sorted_by_d = list(sorted(nums, key=lambda x: (x[1][1], x[1][0])))
        d_of_nums = []
        for i in nums:
            d_of_nums.append(i[1][0])
            d_of_nums.append(i[1][1])
        d_of_nums.sort()
        print(d_of_nums[0])
    else:
        pass
