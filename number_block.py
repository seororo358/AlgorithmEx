import math


def solution(begin, end):
    answer = [0] * (end - begin + 1)
    num = begin

    for i in range(begin, end + 1):
        answer[i-begin] = 1
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0 and i//j <= 10000000:
                answer[i-begin] = i // j
                break


    if begin == 1:
        answer[0] = 0

    return answer


print(solution(999999990, 1000000000))
