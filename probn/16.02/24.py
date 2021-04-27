s = input().lower()

curr = ["x", "y", "z"]
cur_ind = 0
maxk = 0
k = 0
for i in range(len(s)):
    if s[i] == curr[cur_ind]:
        k += 1
        cur_ind = (cur_ind + 1) % 3
    else:
        cur_ind = 0
        maxk = max(maxk, k)

        k = 0
        if s[i] == curr[cur_ind]:
            k += 1
            cur_ind += 1
maxk = max(maxk, k)
print(maxk)
