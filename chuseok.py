def solution(lines):
    times = []
    find = []
    for i in lines:
        date, time, sec = i.split(" ")
        time = time.split(":")
        hour, minute, second = int(time[0]), int(time[1]), float(time[2])
        sec = float(sec[:-1])
        start = 3600*hour + 60*minute + second-sec + 0.001
        end = 3600*hour + 60*minute + second
        times.append([round(start,3),round(end,3)])

    times.sort(key= lambda x: x[1])

    for i in times:
        temp = [i[1],i[1]+1]
        answer = 0
        for j in times:
            if temp[0] <= j[1] < temp[1] or temp[0] <= j[0] < temp[1] or (temp[0] >= j[0] and temp[1] < j[1]):
                answer += 1
        find.append(answer)

    return max(find)
print(solution(["2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"]))

