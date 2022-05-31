def date2int(string):
    repo = [1000*60*60,1000*60,1000]
    
    s = string.split()
    temp = 0
    for i in range(3):
        temp += int(float(s[1].split(":")[i])*repo[i])
    
    t = int(float(s[2][:-1])*1000)
    
    return temp, t

def solution(lines):
    n = len(lines)
    
    repo = []
    for l in lines:
        end, T = date2int(l)
        repo.append((end-T+1,end))
    
    # search
    ans = 0
    for i in range(n):
        cnt = 0
        time = repo[i][1]
        for j in range(i,n):
            start,end = repo[j]
            if time+999 >= start:
                cnt += 1
        ans = max(ans, cnt)
    return ans
            