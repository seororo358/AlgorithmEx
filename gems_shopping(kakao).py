def solution(gems):
    gemset = set(gems)
    leng_set = len(gemset)
    gem_dic = {}
    leng_dic = 0
    start = 0
    found_all = False
    q = []

    for i in range(len(gems)):
        if gems[i] not in gem_dic.keys():
            gem_dic[gems[i]] = 1
            leng_dic += 1
            if leng_dic == leng_set:
                found_all = True
                last = i+1
                for lo in range(start, last):
                    gem_dic[gems[lo]] -= 1
                    if gem_dic[gems[lo]] == 0:
                        start = lo + 1
                        q.append((abs(last - start), start, last))
                        break
        else:
            gem_dic[gems[i]] += 1
            if gem_dic[gems[i]] == 1 and found_all:
                last = i+1
                for lo in range(start, last):
                    gem_dic[gems[lo]] -= 1
                    if gem_dic[gems[lo]] == 0:
                        start = lo + 1
                        q.append((abs(last - start), start, last))
                        break

    q.sort(key=lambda x: x[0])

    answer = [q[0][1], q[0][2]]

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA", "RUBY"]))
