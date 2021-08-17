def solution(n, s, a, b, fares):

    INF = 1e7

    mapping = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(0, n + 1):
        mapping[i][i] = 0
    for i in fares:
        mapping[i[0]][i[1]], mapping[i[1]][i[0]] = i[2], i[2]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if mapping[i][j] == INF:
                continue
            for k in range(1, n + 1):
                if mapping[i][j] + mapping[j][k] < mapping[i][k]:
                    mapping[i][k] = mapping[i][j] + mapping[j][k]
                    mapping[k][i] = mapping[i][k]
                else:
                    pass

    not_with = mapping[a][s] + mapping[b][s]
    with_ma = min(mapping[a][i] + mapping[b][i] + mapping[s][i] for i in range(1,n+1))
    if not_with < with_ma:
        return not_with
    else:
        return with_ma

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))