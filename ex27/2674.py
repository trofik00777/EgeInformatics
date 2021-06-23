with open("datasets/27-14test.txt", "r") as f:
    a = f.read().strip().split("\n")

n = int(a[0])
data = [0 for _ in range(12)]

for i in a[1:]:
    h = int(i)
    data[h % 12] += 1

print(data[:])

print(data[1] * data[11] +
      data[2] * data[10] +
      data[3] * data[9] +
      data[4] * data[8] +
      data[5] * data[7] +
      (data[6] - 1) * (data[6] - 1) +
      (data[0] - 1) * (data[0] - 1))
