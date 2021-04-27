n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

c = min(data)
mink = float("inf")
for i in range(n):
    if data[i] % 2 != 0 and data[i] <= mink / c:
        a = [data[j] for j in range(i + 6, n) if data[j] % 2 != 0]
        if a:
            cond = min(a)
            mink = min(mink, data[i] * cond)

        # for j in range(i + 6, n):
        #     if data[j] % 2 != 0:
        #         mink = min(mink, data[i] * data[j])
print(mink)
