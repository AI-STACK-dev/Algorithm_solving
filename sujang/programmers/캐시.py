def findTail(dic):
    for c in dic.keys():
        if dic[c][1] == None:
            return c
    return None

def findHead(dic):
    for c in dic.keys():
        if dic[c][0] == None:
            return c
    return None

def solution(cs, cities):
    repo = {}
    ans = 0
    for c in cities:
        c = c.lower()
        if c in repo:
            prev,nex = repo[c]
            if prev!=None:
                repo[prev][1] = nex
            if nex!=None:
                repo[nex][0] = prev
            del repo[c]
            tail = findTail(repo)
            if tail == None:
                repo[c] = [None,None]
            else:
                repo[tail][1] = c
                repo[c] = [tail,None]
            ans += 1
        elif cs > 0:
            if len(repo)==0:
                repo[c] = [None, None]
            else:
                tail = findTail(repo)
                repo[tail][1] = c
                repo[c] = [tail,None]
            ans += 5
            cs -= 1
        else:
            if len(repo) > 0:
                head, tail = findHead(repo), findTail(repo)
                nxt = repo[head][1]
                del repo[head]
                if nxt != None:
                    repo[nxt][0] = None
                    repo[tail][1] = c
                    repo[c] = [tail,None]
                else:
                    repo[c] = [None,None]
            ans += 5
    return ans
