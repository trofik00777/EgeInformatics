with open("datasets/27-61a.txt", "r") as f:
    a = f.read().strip().split("\n")

n = int(a[0])
nums = [int(i) for i in a[1:]]
nums.sort()

traectory = [0 for _ in range(sum(nums) + 1)]
traectory[0] = 1
