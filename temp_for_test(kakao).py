from itertools import combinations_with_replacement as cwr


def solution(board, skill):
    answer = 0
    row = len(board)
    col = len(board[0])
    for sk in skill:
        if sk[0] == 1:
            for i in range(sk[1],sk[3]+1):
                for j in range(sk[2],sk[4]+1):
                    board[i][j] -= sk[5]
        elif sk[0] == 2:
            for i in range(sk[1],sk[3]+1):
                for j in range(sk[2],sk[4]+1):
                    board[i][j] += sk[5]
    for i in range(0,row):
        for j in range(col):
            if board[i][j] > 0:
                answer += 1
    return answer


print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
