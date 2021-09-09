def solution(n, build_frame):
    build_frame_set = {0: {}, 1: {}}
    mapping = [[-1] * (n+1) for _ in range(n+1)]

    for q in build_frame:
        if q[3] == 1:
            if q[2] == 0:
                if q[1] == 0 or ((q[0],q[1]-1) in build_frame_set[0]) or ((q[0]-1,q[1]) in build_frame_set[1]):
                    build_frame_set[0].add(tuple(q[:2]))
                else:
                    continue
            elif q[2] == 1:
                if ((q[0],q[1]-1) in build_frame_set[0]) or (([0]+1,q[1]-1) in build_frame_set[0]) or ({(q[0]-1,q[1]),(q[0]+1,q[1])} <= build_frame_set[1]):
                    build_frame_set[1].add(tuple(q[:2]))
                else:
                    continue
        elif q[3] == 0:
            if q[2] == 0


    temp = list(build_frame_set)
    temp.sort(key = lambda x: (x[0], x[1]))
    answer = []

    for i in temp:
        answer.append(list(i))

    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1],
                      [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
