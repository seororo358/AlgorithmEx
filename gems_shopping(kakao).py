def solution(gems):
    answer = []
    least = []
    gemset = set(gems)
    length = len(gemset)
    last = 0
    start = 0

    for i in range(len(gems),0,-1):
        if len(set(gems[:i])) == length:
            continue
        else:
            last = i + 1
            break
        last = 1

    for i in range(0,len(gems)):
        temp = len(set(gems[i:last]))
        if temp == length:
            continue
        else:
            start = i
            break
        start = 1

    answer = [start,last]
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))