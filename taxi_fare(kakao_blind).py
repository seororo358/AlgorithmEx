import math
## 플로이드 와샬
import math


def solution(n, s, a, b, fares):
    INF = math.inf
    mapping = [[INF] * n for _ in range(n)]

    for i in range(0, n):
        mapping[i][i] = 0

    for i in fares:
        mapping[i[0] - 1][i[1] - 1], mapping[i[1] - 1][i[0] - 1] = i[2], i[2]
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if mapping[i][j] > mapping[i][k] + mapping[k][j]:
                    mapping[i][j] = mapping[i][k] + mapping[k][j]
                    mapping[j][i] = mapping[i][j]
                else:
                    pass

    # a노드와 b노드의 모든 최단거리를 거치면서 최솟값을 계산

    return min([mapping[a - 1][i] + mapping[b - 1][i] + mapping[s - 1][i] for i in range(0, n)])


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))