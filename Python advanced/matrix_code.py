n = int('6')
board = [['0'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i + j >= n - 1 and i - j >= 0) or (i - j <= 0 and i + j <= n - 1):
            board[i][j] = '1'

for row in board:
    print(*row)

