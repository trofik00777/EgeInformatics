with open("datasets/27-38b.txt", "r") as f:
    a = f.read().strip().split("\n")

n = int(a[0])
nums = dict()
answ = " "
ost = []

for i in a[1:]:
    c = int(i)
    if c in nums:
        nums[c] += 1
    else:
        nums[c] = 1

print(nums)
ns = list(sorted(nums.keys(), key=lambda x: -x))

print(ns)

for i in ns:
    k = nums[i]
    if k > 1:
        k1 = k // 2
        answ = answ.replace(" ", f"{str(i) * k1} {str(i) * k1}")
        nums[i] -= k1 * 2
        if nums[i] > 0:
            ost.append(i)
    else:
        ost.append(i)

if ost:
    answ = answ.replace(" ", str(max(ost)))

print(answ)
print(sum(int(i) for i in answ))
