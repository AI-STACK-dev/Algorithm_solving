def solution(s):
    ans = len(s)
    for step in range(1,(len(s)//2)+1):
        string = ''
        prev = s[0:step]
        cnt = 1
        for nxt in range(step,len(s),step):
            if prev == s[nxt:nxt+step]:
                cnt +=1
            else:
                if cnt == 1:
                    string += prev
                else:
                    string += str(cnt)+prev
                cnt = 1
                prev = s[nxt:nxt+step]
        
        string += str(cnt)+prev if cnt>1 else prev
        ans = min(len(string),ans)
    return ans                