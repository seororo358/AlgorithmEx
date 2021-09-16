from itertools import product as pr
from itertools import combinations as comb

def solution(user_id, banned_id):
    answer = 0
    answer_set = set()
    ban = dict()
    for user in user_id:
        for banned in banned_id:
            true_tb = True
            if len(user) != len(banned):
                continue
            else:
                for i in range(len(banned)):
                    if banned[i] == '*':
                        pass
                    elif banned[i] != user[i]:
                        true_tb = False
                        break
                    else:
                        pass
            if true_tb:
                if user not in ban.keys():
                    ban[user] = set()
                    ban[user].add(banned)
                else:
                    ban[user].add(banned)

    for user in ban.keys():
        ban[user] = list(ban[user])

    for combi in comb(ban.keys(),len(banned_id)):
        st = []
        for temp in combi:
            st.append(ban[temp])

        for prod in list(pr(*st)):
            if sorted(banned_id) == sorted(prod):
                answer_set.add(tuple(sorted(combi)))

    answer = len(answer_set)

    return answer


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
                ["fr*d*", "abc1**"]))
