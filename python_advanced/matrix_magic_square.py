n = int(input())
allowed_nums = [num for num in range(1, 1 + pow(n, 2))]
matr = [input().split() for _ in range(n)]


def check_matrix(matr):

    if sum([int(matr[i][i]) for i in range(n)]) != sum([int(matr[i][n - i - 1]) for i in range(n)]): 
        return 'NO'
    
    all_nums = []
    for i in range(n):
        for j in range(n):
            all_nums.append(int(matr[i][j]))
            if int(matr[i][j]) not in allowed_nums:
                return 'NO'

    if len(all_nums) != len(set(all_nums)):
            return 'NO'

    # for i in range(n):
    #     if len([int(matr[i][j]) for j in range(n)]) != len(set([int(matr[i][j]) for j in range(n)])):
    #         return 'NO'
    
    # for j in range(n):
    #     if len([int(matr[i][j]) for i in range(n)]) != len(set([int(matr[i][j]) for i in range(n)])):
    #         return 'NO'

    if [sum([int(matr[i][j]) for j in range(n)]) for i in range(n)] \
    != [sum([int(matr[i][j]) for i in range(n)]) for j in range(n)]:
        return 'NO'
    
    return 'YES'

print(check_matrix(matr))