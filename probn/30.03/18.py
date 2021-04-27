data = []
for i in range(1000):
    data.append(int(input()))
print(data)
k = 0
for i in range(len(data)):
    a = data[i]
    for j in range(i + 11, len(data)):
        b = data[j]
        if a + b < 200:
            k += 1

print(k)
