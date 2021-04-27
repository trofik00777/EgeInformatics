n = int(input())

nums = []
for i in range(n):
    a, b = sorted(map(int, input().split()))

    nums.append([a, b, b - a])

s = sum(i[1] for i in nums)
if s % 3:
    print(s)
    exit()
else:
    a = [i[-1] for i in nums if i[-1] % 3]
    print(s - min(a))
