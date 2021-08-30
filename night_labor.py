import heapq as hq

def solution(n, works):
    answer = 0
    heap = []

    if n >= sum(works):
        return 0
    for work in works:
        hq.heappush(heap, (-work, work))

    while n > 0:
        num = hq.heappop(heap)[1] - 1
        hq.heappush(heap, (-num, num))
        n -= 1

    for i in heap:
        answer += i[1] ** 2

    return answer