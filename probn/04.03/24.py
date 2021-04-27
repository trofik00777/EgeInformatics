s = input()
s = s.replace("C", "D")
print(s)
a = [len(i) for i in s.split("D")]
print(max(a))
