def solution(priorities, location):
    answer = 0
    q = []

    while priorities:
        answer += 1
        top = max(priorities)

        if location < 0:
            location += len(priorities)

        for i in range(0,len(priorities)):
            if priorities[i] != top:
                q.append(priorities[i])
                location -= 1
            else:
                if location == 0:
                    return answer
                else:
                    priorities += q
                    del priorities[0:i + 1]
                    if location > 0:
                        location -= 1
                    del q[:]
                    break

    return answer
print(solution([1, 1, 9, 1, 1, 1],0))