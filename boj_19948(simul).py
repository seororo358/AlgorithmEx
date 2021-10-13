import sys
arr = list(sys.stdin.readline().split())
space = int(sys.stdin.readline())
alphabet = dict()
alph_num = list(map(int, sys.stdin.readline().split()))
ch = 'a'
k = 0

while k < 26:
    alphabet[ch] = alph_num[k]
    ch = chr(ord(ch)+1)
    k += 1

ans = True
if space < len(arr) - 1:
    ans = False
if ans:
    for i in arr:
        item = i.lower()
        alphabet[item[0]] -= 1
        if alphabet[item[0]] < 0:
            ans = False
            break
if ans:
    for i in arr:
        item = i.lower()
        char = ''
        for j in item:
            if j == char:
                continue
            alphabet[j] -= 1
            char = j
            if alphabet[j] < 0:
                ans = False
        if not ans:
            break

if not ans:
    print(-1)
else:
    temp = []
    for i in arr:
        temp.append(i[0])
    answer = ''.join(temp)
    print(answer.upper())
