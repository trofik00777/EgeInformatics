with open("24-171.txt", "r") as f:
    lines = f.read().strip().split()

max_k = -1
for s in lines:
    i = 0
    k = 0
    while i < len(s):
        if s[i:i + 3] == "XYZ":
            if k == 0:
                if s[i - 1] in "XYZ":
                    k += 1
            k += 3
            i += 3
        else:
            if k != 0:
                if s[i] in "XYZ":
                    k += 1
            max_k = max(max_k, k)
            k = 0
            i += 1

print(max_k)
