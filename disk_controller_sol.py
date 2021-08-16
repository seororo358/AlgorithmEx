import heapq as hq

def solution(jobs):
    time = 0
    working = False
    dp = []
    heap = []
    jobs.sort(key=lambda x: x[0], reverse=True)

    while jobs:
        if not working:
            working = True
            time = jobs[-1][1] + jobs[-1][0]
            dp.append(jobs[-1][1])
            jobs.pop()

        while working:
            if jobs and time >= jobs[-1][0]:
                hq.heappush(heap, (jobs[-1][1], jobs[-1][0]))
                jobs.pop()
            else:
                if not heap:
                    working = False
                    break
                else:
                    time += heap[0][0]
                    dp.append(time - heap[0][1])
                    hq.heappop(heap)

    answer = sum(dp) // len(dp)
    return answer

print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))