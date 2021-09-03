def solution(gems):
    gemset = set(gems)
    leng_set = len(gemset)
    gem_dic = {}
    leng_dic = 0
    last = 0
    start = 0

    for i in range(len(gems)):
        if gems[i] not in gem_dic.keys():
            gem_dic[gems[i]] = 1


        else:
            gem_dic[gems[i]] += 1




    answer = [start, last]

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA", "RUBY"]))
