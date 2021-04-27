n = int(input())
nums = []
for _ in range(n):
    nums.append(list(sorted(map(int, input().split()))))
max_sum = sum([i[-1] for i in nums]) % 10
min_sum = sum([i[0] for i in nums])
if max_sum == min_sum % 10:
    print(min_sum)
    exit()
else:
    last_n = [float("inf") for _ in range(10)]
    last_n[nums[0][0] % 10] = min(last_n[nums[0][0] % 10], nums[0][0])
    last_n[nums[0][1] % 10] = min(last_n[nums[0][1] % 10], nums[0][1])
    for pair in nums[1:]:
        n1, n2 = pair

        variants = [float("inf") for _ in range(10)]
        for num in last_n:
            if num < float("inf"):
                x1 = num + n1
                x2 = num + n2
                variants[x1 % 10] = min(variants[x1 % 10], x1)
                variants[x2 % 10] = min(variants[x2 % 10], x2)
        # concat = []
        # for i in range(10):
        #     if variants[i] < float("inf"):
        #         concat.append(variants[i])
        #     else:
        #         concat.append(last_n[i])
        # last_n = concat[:]
        last_n = variants[:]
    print(last_n[max_sum])
