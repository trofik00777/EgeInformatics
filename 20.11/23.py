from pprint import pprint

answ = []


def f(traectory, n):
    if n == 20:
        answ.append("".join([ str(i) for i in traectory]))
        return
    if n + 1 <= 20:
        f(traectory + [n + 1], n + 1)
    if n * 2 <= 20:
        f(traectory + [n * 2], n * 2)


f([], 1)
pprint(list(set([i for i in answ if "10" in i])))
