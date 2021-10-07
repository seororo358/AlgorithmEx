# 0: left #1: right #2: up #3: down
def solution(n, m, x, y, queries):
    answer = 0
    max_t = n * m
    pos = [[x, y], [x, y]]
    temp = 1
    while queries:
        command = queries.pop()
        if command[0] == 0:  # left
            if pos[0][1] == 0:  # pos시작 y값이 0
                pos[1][1] += min(command[1], m - 1 - pos[1][1])
            else:
                pos[0][1] += command[1]
                pos[1][1] += command[1]
                if pos[1][1] >= m:
                    if pos[0][1] >= m:
                        return 0
                    else:
                        pos[1][1] = m - 1
        elif command[0] == 1:  # right
            if pos[1][1] == m - 1:  # pos끝 y값이 m-1
                pos[0][1] -= min(command[1], pos[0][1])
            else:
                pos[0][1] -= command[1]
                pos[1][1] -= command[1]
                if pos[0][1] < 0:
                    if pos[1][1] < 0:
                        return 0
                    else:
                        pos[0][1] = 0
        elif command[0] == 2:  # up
            if pos[0][0] == 0:  # pos끝 y값이 m-1
                pos[1][0] += min(command[1], n - 1 - pos[1][0])
            else:
                pos[0][0] += command[1]
                pos[1][0] += command[1]
                if pos[1][0] >= n:
                    if pos[0][0] >= n:
                        return 0
                    else:
                        pos[1][0] = n - 1
        else:  # down
            if pos[1][0] == n - 1:  # pos끝 y값이 m-1
                pos[0][0] -= min(command[1], pos[0][0])
            else:
                pos[0][0] -= command[1]
                pos[1][0] -= command[1]
                if pos[0][0] < 0:
                    if pos[1][0] < 0:
                        return 0
                    else:
                        pos[0][0] = 0
        if pos[0] == [0, 0] and pos[1] == [n - 1, m - 1]:
            break
    answer = (pos[1][0] - pos[0][0] + 1) * (pos[1][1] - pos[0][1] + 1)

    return answer