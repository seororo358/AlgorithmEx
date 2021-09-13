import heapq as hq


def solution(n, cores):
    answer = 0
    q = []
    length = len(cores)
    time = 0
    i = 0

    if len(cores) >= n:
        return cores[n - 1]
    while n > 0:
        if len(q) < length:
            hq.heappush(q, (time + cores[i], i, n))
            i += 1
            n -= 1
        else:
            time, index, count = q[0]
            while q:
                if time == q[0][0]:
                    core, count = hq.heappop(q)[1:]
                    hq.heappush(q, (time + cores[core], core, n))
                    n -= 1
                    if n == 0:
                        answer = core + 1
                        break
                else:
                    break

    return answer


print(solution(7, [1, 2, 3]))
