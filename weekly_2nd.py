def solution(scores):
    answer = ''

    for i, tp in enumerate(zip(*scores)):
        temp = list(tp)
        mi = min(tp)
        ma = max(tp)
        if temp[i] == mi and temp.count(mi) == 1:
            avg = (sum(temp) - mi) / (len(temp)-1)
        elif temp[i] == ma and temp.count(ma) == 1:
            avg = (sum(temp) - ma) / (len(temp)-1)
        else:
            avg = sum(temp) / len(temp)
        if avg >= 90:
            answer += 'A'
        elif 80 <= avg < 90:
            answer += 'B'
        elif 70 <= avg < 80:
            answer += 'C'
        elif 50 <= avg < 70:
            answer += 'D'
        else:
            answer += 'F'

    return answer
