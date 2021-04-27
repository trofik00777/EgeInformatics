k = 0
n_max = 0
for i in range(1016, 7938):
    if i % 3 == 0 and i % 7 and i % 17 and i % 19 and i % 27:
        k += 1
        if i > n_max:
            n_max = i
print(k, n_max)
