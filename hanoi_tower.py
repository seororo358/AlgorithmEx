import copy

def solution(n):
    temp = 1
    answer = [[1, 3]]

    if n == 1:
        return answer
    while temp <= n:
        temp += 1
        tower = copy.deepcopy(answer)
        for i in range(len(answer)):
            for j in range(0, 2):
                if answer[i][j] == 2:
                    answer[i][j] = 3
                elif answer[i][j] == 3:
                    answer[i][j] = 2
                else:
                    pass
        answer.append([1, 3])
        for i in range(len(tower)):
            for j in range(0, 2):
                if tower[i][j] == 1:
                    tower[i][j] = 2
                elif tower[i][j] == 2:
                    tower[i][j] = 1
                else:
                    pass
        answer += tower

    return answer