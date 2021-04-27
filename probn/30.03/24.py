s = input()

all_k = 0
k = 1
for i in range(1, len(s)):
    if s[i] > s[i - 1]:
        k += 1
    else:
        if k == 5:
            all_k += 1
        k = 1
print(all_k)
