k = []

for i in range(127, 9852 + 1):
    if i % 3 == 0 and i % 9 != 0:
        if len(oct(i)[2:]) == len(str(i)):
            k.append(i)

print(k)
print(len(k))
print(max(k))
