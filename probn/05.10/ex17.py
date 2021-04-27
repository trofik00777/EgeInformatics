answ = []

for i in range(4668, 10415):
    if (i % 3 == 0 or i % 11 == 0) and i % 2 and i % 13 and i % 22 and i % 33:
        answ.append(i)
print(len(answ), min(answ))
