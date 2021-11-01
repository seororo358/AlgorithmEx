import sys
input = sys.stdin.readline

def product_mat(mat):
    arr = [[sum([mat[i][j] * mat[j][k] for j in range(n)]) % 1000 for k in range(n)]
           for i in range(n)]
    return arr

def conv(mat1, mat2):
    arr = [[sum([mat1[i][j] * mat2[j][k] for j in range(n)]) % 1000 for k in range(n)]
           for i in range(n)]
    return arr

def matrix_conv(mat, x):
    if x == 1:
        for i in range(n):
            for j in range(n):
                mat[i][j] %= 1000
        return mat
    if x % 2:
        return conv(matrix_conv(mat, x-1), mat)
    else:
        return matrix_conv(product_mat(mat), x//2)


n, b = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
board = matrix_conv(board, b)
for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j], end=" ")
    print()
