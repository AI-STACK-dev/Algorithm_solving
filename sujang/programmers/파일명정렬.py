import re
def solution(files):
    repo = []
    for i,F in enumerate(files):
        f = F.lower()
        temp = re.split('(\d+)',f,maxsplit=1)
        repo.append((temp[0],int(temp[1]),i,F))
    repo.sort(key=lambda x : (x[0],x[1],x[2]))
    
    ans = []
    for e in repo:
        ans.append(e[-1])
    return ans
    