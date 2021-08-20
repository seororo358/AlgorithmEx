def solution(s):
    answer = 0
    q = []
    for i in range(1,len(s)+1):
        window = s[0:i]
        q.append()
        for j in range(i,len(s)+1-i):
            if s[j:j+i] == window:
                q.append

    return answer