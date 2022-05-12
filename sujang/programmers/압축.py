def solution(msg):
    # init
    repo = {}
    for i in range(26):
        repo[chr(ord('A') + i)] = i+1
    
    # calculate
    ans = []
    curr = 26
    i,n = 0,len(msg)
    while i < n:
        for j in range(i,n+1):
            if msg[i:j+1] in repo:
                temp = repo[msg[i:j+1]]
            else:
                break
        repo[msg[i:j+1]] = curr+1
        curr += 1
        ans.append(temp)
        i = j
        
    return ans