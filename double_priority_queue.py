import heapq as hq

def solution(operations):
    answer = []
    q = []
    for i in operations:
        arr = i.split(" ")
        if arr[0] == "D" and q:
            if arr[1] == "-1":
                hq.heappop(q)
            else:
                q = hq.nlargest(len(q), q)[1:]
                hq.heapify(q)

        elif arr[0] == "I":
            hq.heappush(q,int(arr[1]))
    if not q:
        return [0,0]
    else:
        q.sort()
        return [q[-1],q[0]]


print(solution(["I 7","I 5","I -5","D -1"]))