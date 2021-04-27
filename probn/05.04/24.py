s = input()

l = 1
max_l = 0
ind_answ = -1
curr_ind = 1

for i in range(1, len(s)):
    if s[i] < s[i - 1]:
        l += 1
    else:
        if l > max_l:
            max_l = l
            ind_answ = curr_ind
        l = 1
        curr_ind = i + 1

print(max_l, ind_answ)
