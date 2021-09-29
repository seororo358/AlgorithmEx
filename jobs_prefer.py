def solution(table, languages, preference):
    answer = ''
    ans_tb = dict()
    job = dict()
    for tb in table:
        temp = tb.split()
        job[temp[0]] = temp[1:]
        ans_tb[temp[0]] = 0

    for j in job.keys():
        score = 0
        for k in range(len(languages)):
            for i in range(len(job[j])):
                if job[j][i] == languages[k]:
                    score += (5-i) * preference[k]
                    break
        ans_tb[j] = score
    top = 0
    for ans in ans_tb.keys():
        if ans_tb[ans] > top:
            answer = ans
            top = ans_tb[ans]
        elif ans_tb[ans] == top:
            if ans > answer:
                pass
            else:
                answer = ans

    return answer

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
               ["PYTHON", "C++", "SQL"], [7, 5, 5]))
