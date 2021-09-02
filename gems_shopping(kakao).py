def solution(gems):
    gemset = len(set(gems))
    gem_dic = {}
    last = 1
    start = 1

    for gem in gems:
        if gem not in gem_dic.keys():
            gem_dic[gem] = 1
        else:
            gem_dic[gem] += 1
        if 0 not in gem_dic.values() and gemset == len(gem_dic.keys()):
            break
        else:
            last += 1

    for gem in gems:
        gem_dic[gem] -= 1
        if gem_dic[gem] == 0:
            break
        else:
            start += 1

    answer = [start, last]

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
