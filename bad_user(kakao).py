from itertools import product as pr
def solution(user_id, banned_id):
    answer = 0
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
                if banned not in ban.keys():
                    ban[banned] = set()
                    ban[banned].add(user)
                else:
                    ban[banned].add(user)
    st = list(ban.values())


    return st


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))
