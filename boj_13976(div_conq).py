import sys
input = sys.stdin.readline
inf = 1000000007


def conv(arr1, arr2):
    matrix = [[0,0],[0,0]]
    matrix[0][0] = (arr1[0][0]*arr2[0][0] + arr1[0][1]*arr2[1][0])
    matrix[0][1] = (arr1[0][0]*arr2[0][1] + arr1[0][1]*arr2[1][1])
    matrix[1][0] = (arr1[1][0]*arr2[0][0] + arr1[1][1]*arr2[1][0])
    matrix[1][1] = (arr1[1][0]*arr2[0][1] + arr1[1][1]*arr2[1][1])
    for i in range(2):
        for j in range(2):
            if matrix[i][j] < 0:
                continue
            matrix[i][j] %= inf
    return matrix


def div_conq(x):
    if x in mat_dic.keys():
        return mat_dic[x]
    if x % 2:
        mat_dic[x] = conv(div_conq(x-1), mat_dic[1])
    else:
        mat_dic[x] = conv(div_conq(x//2), div_conq(x//2))
    return mat_dic[x]


n = int(input())
if n % 2 or n == 0:
    print(0)
else:
    arr = [[3], [1]]
    mat_dic = {0: [[1,0],[0,1]], 1: [[4,-1],[1,0]]}
    fin_mat = div_conq(n//2-1)
    answer = (fin_mat[0][0] * arr[0][0] + fin_mat[0][1] * arr[1][0]) % inf
    print(answer)
