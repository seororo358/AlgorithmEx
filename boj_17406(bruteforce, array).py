import sys
from itertools import permutations
import copy


def rotate(a, row, col, step):
    for st in range(1, step+1):
        temp = a[row - st][col - st]
        for i in range(row - st, row + st):
            a[i][col - st] = a[i+1][col - st]
        for i in range(col - st, col + st):
            a[row + st][i] = a[row + st][i+1]
        for i in range(row + st, row - st, -1):
            a[i][col + st] = a[i-1][col + st]
        for i in range(col + st, col - st + 1, -1):
            a[row - st][i] = a[row - st][i-1]
        a[row - st][col - st + 1] = temp


n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
q = []
for _ in range(k):
    q.append(list(map(int, sys.stdin.readline().split())))
answer = []
for queries in permutations(q, k):
    t_arr = copy.deepcopy(arr)
    for query in queries:
        rotate(t_arr, query[0]-1, query[1]-1, query[2])
    answer.append(min(sum(t_arr[i]) for i in range(n)))

print(min(answer))
