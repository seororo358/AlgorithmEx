def solution(info, query):
    answer = []
    num = 1
    volunteer = {}
    #정보 딕셔너리에 저장
    for i in info:
        lang, job, time, food, score = i.split()
        volunteer[num] = ({lang, job, time, food}, int(score))
        num += 1
    #쿼리대로 처리
    for q in query:
        temp = q.split()
        plus = 0
        lang, job, time, food, score = temp[0], temp[2], temp[4], temp[6], int(temp[7])
        q_set = {lang,job,time,food}
        q_set -= {'-'}
        for value in volunteer.values():
            if value[0] | q_set == value[0] and score <= value[1]:
                plus += 1 #정보확인시 +1

        answer.append(plus)

    return answer


print(solution(["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"],
               ["java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"]))
