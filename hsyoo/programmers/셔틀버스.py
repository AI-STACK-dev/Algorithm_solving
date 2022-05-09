def solution(n, t, m, timetable):
    answer = ''
    start_time = 9 * 60
    buses = [start_time + i*t for i in range(n)]
    arrival = []
    for arv in timetable:
        h,minute = arv.split(':')
        num = int(h)*60 + int(minute)
        if num <= buses[-1]:
            arrival.append(num)
    
    arrival.sort()

    start = 0
    for idx, bus in enumerate(buses):
        cnt = 0
        # print(arrival[start:], start)
        if idx == len(buses)-1:
            if len(arrival[start:]) >= m:
                time = arrival[-1]
                # while 
                while len([i for i in arrival[start:] if i <= time]) > m-1:
                    time -= 1
            else:
                time = bus
        else:
            if len(arrival[start:]) == 0:
                time = buses[-1]
                break
            else:
                while start <= len(arrival)-1 and arrival[start] <= bus and cnt < m:
                    start += 1
                    cnt += 1
    div = str(time // 60)
    res = str(time % 60)
    answer = div.rjust(2, '0') + ':' + res.rjust(2, '0')
    return answer

# print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]	))
# print(solution(2,10,2,["09:10", "09:09", "08:00"]))
# print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
# print(solution(1,1,5,["00:01", "00:01", "00:01", "00:01", "00:01"]))
# print(solution(1,1,1,["23:59"]	))
print(solution(2,30,1,["09:00"]	))

# print(solution(10,60,45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))