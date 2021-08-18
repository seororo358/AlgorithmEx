def solution1(n, edges):
    step = 0
    q = [1]
    tb = [-1] * (n + 1)
    tb[1] = 0
    matrix = [[0] * (n+1) for _ in range(0,n+1)]

    for edge in edges:
        matrix[edge[0]][edge[1]] = 1
        matrix[edge[1]][edge[0]] = 1
    while q:
        st = []
        for i in q:
            for j in range(1,n+1):
                if matrix[i][j] == 1 and tb[j] == -1:
                    st.append(j)
                elif matrix[i][j] == 1 and tb[j] == -1:
                    st.append(j)
                else:
                    pass
        del q[:]
        if st:
            step += 1
            q += list(set(st))
            for i in q:
                tb[i] = step
        else:
            pass
    answer = tb.count(step)
    return answer

### 인접행렬(연결된 노드 표현 방식)
def solution2(n, edges):
    step = 0
    q = [1]
    tb = [-1] * (n + 1)
    tb[1] = 0
    matrix = [[] for _ in range(0,n+1)]

    for edge in edges:
        matrix[edge[0]].append(edge[1])
        matrix[edge[1]].append(edge[0])
    while q:
        st = []
        for i in q:
            for j in range(len(matrix[i])):
                if tb[matrix[i][j]] == -1:
                    st.append(matrix[i][j])
                else:
                    pass
        del q[:]
        if st:
            step += 1
            q += list(set(st))
            for i in q:
                tb[i] = step
        else:
            pass
    answer = tb.count(step)
    return answer