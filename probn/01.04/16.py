C = 0

def F(n):
    global C
    C += 1
    if n >= 1:
        C += 1
        F(n - 1)
        F(n // 2)


F(140)
print(C)
