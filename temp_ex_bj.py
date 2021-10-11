import bisect as bi
N, M = map(int, input().split())
arr = []
query = []
answer = []
for _ in range(N):
    arr.append(int(input()))

for _ in range(M):
    query.append(int(input()))
arr.sort()
for i in query:
    temp = bi.bisect_left(arr, i)
    if temp == len(arr):
        answer.append(-1)
    else:
        if arr[temp] == i:
            answer.append(temp)
        else:
            answer.append(-1)

for i in answer:
    print(i)
