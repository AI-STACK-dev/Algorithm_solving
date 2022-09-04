# 셔틀은 9시부터 총 n회 t분 간격으로 역에 도착, 최대 m명이 탈 수 있음.
# 대기순서대로 태우고 출발, 9시에 도착했는데, 자리가 있다면 9시에도 탈 수 있음.
# 같은 시각에 도착한 크루 중 대기열에서 제일 뒤에 선다. 23시 59분에는 집에 돌아감.

# 시간을 시와 분으로 나누고 int 형태로 바꾼다. 나중에는 int를 다시 나눠서 시간 형태로 만들어주면됨. 그리고 정렬
# 셔틀이 오는 시간을 기준으로 총 언제언제 오는지 알아야함. 
# 각 셔틀이 오는 시간을 기준으로, 탈 수 있다면 셔틀이 도착하는 시간을 result에 저장
# 탈 수 없다면 제일 늦은 크루 -1해서 탈 수 있는지 체크 후, result에 저장.
# 

def time2int(time):
    h, m = time.split(':')
    h, m = int(h) * 60, int(m)
    return h + m

def int2time(num):
    h,m = divmod(num, 60)
    h = '0' + str(h) if len(str(h)) == 1 else str(h)
    m = '0' + str(m) if len(str(m)) == 1 else str(m)
    return h + ':' + m
    
def solution(n, t, m, timetable):
    answer = ''
    start_num = time2int('09:00')
    logs = []
    bus_time = []
    for time in timetable:
        num = time2int(time)
        logs.append(num)
    logs.sort()
    at = start_num
    for i in range(n):
        bus_time.append(at)
        at += t
    
    i = 0
    for bus in bus_time:
        cnt = 0
        while cnt < m and i < len(logs) and logs[i] <= bus:
            i += 1
            cnt += 1
        if cnt < m:
            answer = bus
        else:
            answer = logs[i-1] - 1

    return int2time(answer)

print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]))