with open("Задание 24/24.txt", "r") as f:
    s = f.read().strip()
data = s.split("XZZY")
for i in data:
    print(i)
print(max([(len(i), i) for i in s.split("XZZY")]))
# answ = answ + 6
