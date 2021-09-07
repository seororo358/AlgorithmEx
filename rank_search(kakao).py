def solution(info, query):
    answer = []
    num = 1
    volunteer = {}
    for i in info:
        lang, job, time, food, score = i.split()
        volunteer[num] = (lang, job, time, food, int(score))
        num += 1

    for q in query:
        temp = q.split()
        plus = 0
        lang, job, time, food, score = temp[0], temp[2], temp[4], temp[6], int(temp[7])
        for value in volunteer.values():
            if (lang == value[0] or lang == '-') and (job == value[1] or job == '-') and (time == value[2] or time == '-') \
                    and (food == value[3] or food == '-') and score <= value[4]:
                plus += 1
        answer.append(plus)

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
