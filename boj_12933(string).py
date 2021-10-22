duck = input()
word = ['q', 'u', 'a', 'c', 'k']
visited = [False] * len(duck)
if len(duck) % 5 != 0:
    print(-1)
    exit()
cnt = 0

while True:
    temp = 0
    idx = 0
    for i in range(len(duck)):
        if duck[i] == word[idx] and not visited[i]:
            idx = (idx+1) % 5
            if idx == 0:
                temp += 1
            visited[i] = True
    if temp == 0:
        break
    cnt += 1

for i in visited:
    if not i:
        cnt = -1
        break
print(cnt)
