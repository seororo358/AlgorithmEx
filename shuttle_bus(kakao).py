def solution(n, t, m, timetable):
    time_arr = []
    arrival = []
    last = 0

    for time in timetable:
        hour, minute = time.split(':')
        time_arr.append(int(hour) * 60 + int(minute))

    for i in range(0, n):
        arrival.append(540 + i * t)

    time_arr.sort(reverse=True)
    arrival.reverse()
    while arrival:
        for i in range(m):
            if time_arr and arrival[-1] >= time_arr[-1]:
                last = time_arr.pop() - 1
            else:
                last = arrival[-1]
                break
        arrival.pop()

    answer = str(last // 600) + str((last % 600) // 60) + ":" + str((last % 60) // 10) + str((last % 60) % 10)

    return answer