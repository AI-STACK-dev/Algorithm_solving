def time2int(time: str) -> int:
    h,m = time.split(":")
    return int(h)*60 + int(m)
    
def int2time(time: int) -> str:
    h = time // 60
    m = time % 60
    return str(h).zfill(2) + ":" + str(m).zfill(2)

def solution(n, t, m, timetable):
    tt = list(map(time2int, timetable))
    tt.sort()
    
    bt = [9*60 + t*i for i in range(n)]
    
    i = ans = 0
    for b in bt:
        curr = 0
        while curr < m and i < len(tt) and tt[i]<= b:
            i += 1
            curr += 1
        if curr < m:
            ans = b
        else:
            ans = tt[i-1]-1
    return int2time(ans)