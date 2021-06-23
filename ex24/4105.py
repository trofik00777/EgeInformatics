with open("24-168.txt", "r") as f:
    s = f.read().strip()

counts = []
n = 1
let = s[0]
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        n += 1
    else:
        counts.append((let, n))
        let = s[i]
        n = 1
print(counts)

m_len = -1
length = counts[0][1]
k = 1
for i in range(len(counts) - 2):
    if counts[i][1] <= counts[i + 1][1] <= counts[i + 2][1]:
        length = counts[i][1] + counts[i + 1][1] + counts[i + 2][1]
        m_len = max(m_len, length)

print(m_len)
