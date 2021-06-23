x = int(input())
y = int(input())
a = 0
b = 0
while x > 0 or y>0:
  if x > 0:
    a = a + 1
  if y > 0:
    b = b + 1
  x = x // 2
  y = y // 10
print(a, b)



