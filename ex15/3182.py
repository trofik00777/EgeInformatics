# ДЕЛ(120, A) ∧ (¬ДЕЛ(x, A) → (ДЕЛ(x, 36) → ¬ДЕЛ(x, 15)))

def check(a):
    for y in range(1, 500):
        for x in range(1, 500):
            if not (120 % a == 0 and (x % a == 0 or x % 36 != 0 or x % 15 != 0)):
                return False
    return True


for a in range(120, 0, -1):
    if check(a):
        print(a)
        exit()
