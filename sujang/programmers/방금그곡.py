def hour2minute(time):
    h,m = map(int,time.split(":"))
    return h*60 + m

def infoParser(m):
    i,n = 0,len(m)
    temp = []
    while i < n:
        if i != n-1 and m[i+1] == "#":
            temp.append(m[i:i+2])
            i += 1
        else:
            temp.append(m[i:i+1]+" ")
        i += 1
    return temp
        
def returnFullMusicInfo(m, amt):
    temp = []
    n = len(m)
    while n < amt:
        temp.extend(m)
        amt -= n
    temp.extend(m[:amt])
    return "".join(temp)

def solution(m, musicinfos):
    n = len(musicinfos)
    temp = []
    m = "".join(infoParser(m))

    for i,j in enumerate(musicinfos):
        k = j.split(",")
        lis = infoParser(k[3])
        time = hour2minute(k[1]) - hour2minute(k[0])
        result = returnFullMusicInfo(lis,time)
        temp.append((result, len(result), i, k[2]))

    ans = []
    for i in range(n):
        if m in temp[i][0]:
            ans.append(temp[i][1:])
    if len(ans) == 0:
        return "(None)"
    ans.sort(key=lambda x : (-x[0],x[1]))
    return ans[0][2]
        