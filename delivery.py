import heapq as hq
INF = int(1e9)

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    distance = [INF for _ in range(N+1)]

    for i in road:
        graph[i[0]].append((i[1],i[2]))
        graph[i[1]].append((i[0],i[2]))

    q = []
    hq.heappush(q, (0, 1))
    distance[1] = 0
    while q:
        dist, now = hq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                hq.heappush(q, (cost, i[0]))
    for i in distance:
        if i <= K:
            answer += 1

    return answer


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
