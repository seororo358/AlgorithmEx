import sys

T = int(sys.stdin.readline())

while T > 0:
    dic = dict()
    find = []
    answer = []
    word = sys.stdin.readline()
    k = int(sys.stdin.readline())
    T -= 1
    idx = 0
    for i in word[:-1]:
        if i not in dic.keys():
            dic[i] = [idx]
        else:
            dic[i].append(idx)
        idx += 1
    for i in dic.keys():
        if len(dic[i]) >= k:
            find.append(i)
    if not find:
        print(-1)
        continue
    for i in find:
        for j in range(len(dic[i]) - k + 1):
            answer.append(dic[i][j+k-1] - dic[i][j] + 1)
    print(min(answer), max(answer))
