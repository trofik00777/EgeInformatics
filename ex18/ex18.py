import sys

sums = []


def f(board, row, col, summa):
    s = summa + board[row][col]
    if row == len(board) - 1 and col == len(board[0]) - 1:
        sums.append(s)
        return None
    if row < len(board) - 1:
        f(board, row + 1, col, s)
    if col < len(board[0]) - 1:
        f(board, row, col + 1, s)

b = []
for i in sys.stdin:
    b.append([int(j) for j in i.split()])
f(b, 0, 0, 0)
print(max(sums), min(sums), sums)
