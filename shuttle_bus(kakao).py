def solution(n, t, m, timetable):
    time_arr = []
    arrival = []
    last = 0
    #문자열 분리 및 시간단위 통일
    for time in timetable:
        hour, minute = time.split(':')
        time_arr.append(int(hour) * 60 + int(minute))
    #셔틀버스도착정보
    for i in range(0, n):
        arrival.append(540 + i * t)
    #pop함수 시간복잡도 고려
    time_arr.sort(reverse=True)
    arrival.reverse()
    #셔틀버스에 한명씩 태우기
    while arrival:
        for i in range(m):  #마지막크루 탑승시간을 갱신
            if time_arr and arrival[-1] >= time_arr[-1]:
                last = time_arr.pop() - 1
            else:
                last = arrival[-1]
                break
        arrival.pop()   #셔틀버스를 한대씩 보내기

    answer = str(last // 600) + str((last % 600) // 60) + ":" + str((last % 60) // 10) + str((last % 60) % 10)

    return answer
