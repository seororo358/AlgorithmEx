from collections import deque as dq

N = int(input())
q = dq([i for i in range(1, N+1)])
while len(q) > 1:
    q.popleft()
    cd = q.popleft()
    q.append(cd)
print(q.popleft())
