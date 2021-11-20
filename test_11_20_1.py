def solution(n, horizontal):
    answer = [[0] * n for _ in range(n)]
    pos = [0, 0]
    i = 1
    cnt = 2
    answer[pos[0]][pos[1]] = i
    i += 1

    while cnt <= n:
        if horizontal:
            pos[1] += 1
            for k in range(cnt):
                pos[0] = k
                answer[pos[0]][pos[1]] = i
                i += 1
            for k in range(1, cnt):
                pos[1] -= 1
                answer[pos[0]][pos[1]] = i
                i += 1
            cnt += 1
            horizontal = False
        else:
            pos[0] += 1
            for k in range(cnt):
                pos[1] = k
                answer[pos[0]][pos[1]] = i
                i += 1
            for k in range(1, cnt):
                pos[0] -= 1
                answer[pos[0]][pos[1]] = i
                i += 1
            cnt += 1
            horizontal = True

    return answer


print(solution(4, "true"))
