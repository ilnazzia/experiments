n, m = [int(i) for i in '2 4'.split()]
matr1 = [input().split() for _ in range(n)]
pustaya_stroka = input()
matr2 = [input().split() for _ in range(n)]
matr3 = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matr3[i][j] = int(matr1[i][j]) + int(matr2[i][j])

for row in matr3:
    print(*row)
