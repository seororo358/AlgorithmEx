def solution(distance, rocks, n):
    answer = 0
    min_dis = 1
    max_dis = distance

    rocks.append(distance)
    rocks.append(0)
    rocks.sort()

    while rocks:
        pivot = (min_dis + max_dis) // 2
        temp = 0
        for i in range(1,len(rocks)+1):
            if rocks[i] - rocks[i-1] < pivot:
                temp += 1
        if temp > n:
            max_dis = pivot
            continue
        else:
            r = 1
            while r < len(rocks)+1:
                if rocks[r] - rocks[r-1] == pivot:
                    rocks[r] = rocks[r-1]

    return answer