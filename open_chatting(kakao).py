def solution(record):
    answer = []
    uid_nick = {}
    q = []
    record.reverse()
    while record:
        temp = record[-1].split()
        if temp[0] == "Enter":
            q.append((temp[1],temp[0]))
            uid_nick[temp[1]] = temp[2]
        elif temp[0] == "Leave":
            q.append((temp[1],temp[0]))
        elif temp[0] == "Change":
            uid_nick[temp[1]] = temp[2]
        else:
            pass
        record.pop()

    for uid,order in q:
        if order == "Enter":
            answer.append(uid_nick[uid] + "님이 들어왔습니다.")
        elif order == "Leave":
            answer.append(uid_nick[uid] + "님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))