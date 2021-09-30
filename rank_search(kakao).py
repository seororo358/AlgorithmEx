from itertools import product


def solution(info, query):
    answer = []
    num = 1
    volunteer = dict()
    combi = [["java", "python", "cpp", "-"], ["backend", "frontend", "-"], ["junior", "senior", "-"],
             ["chicken", "pizza", "-"]]

    for item in tuple(product(*combi)):
        volunteer[item] = []

    for i in info:
        lang, job, time, food, score = i.split()
        pd = [[lang, "-"], [job, "-"], [time, "-"], [food, "-"]]
        for prod in tuple(product(*pd)):
            volunteer[prod].append(int(score))

    #쿼리대로 처리

    for q in query:
        temp = q.split()
        plus = 0
        lang, job, time, food, score = temp[0], temp[2], temp[4], temp[6], int(temp[7])
        q_set = (lang, job, time, food)
        for value in volunteer[q_set]:
            if value >= score:
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
