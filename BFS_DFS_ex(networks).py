
def solution(n, computers):
    visit = [0] * (n+1)
    answer = 0
    queue = [1]
    while queue:
        for temp in queue:
            visit[temp] = 1
        st = []
        for i in queue:
            for j in range(n):
                if computers[i-1][j] == 1 and visit[j+1] != 1:
                    st.append(j+1)
                else:
                    pass

        del queue[:]

        if st:
            queue += list(set(st))
        else:
            answer += 1
            for i in range(1,n+1):
                if visit[i] == 0:
                    queue.append(i)
                    break

    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))