def solution(s):
    temp = s.split()
    answer = list(map(int, temp))
    answer.sort()

    return str(answer[0]) + " " + str(answer[-1])

print(solution("-1 -2 -3 -4"))