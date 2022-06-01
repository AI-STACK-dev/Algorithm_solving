from itertools import permutations

def isMatch(uid,banId):
    n = len(uid)
    for i in range(n):
        if len(uid[i]) == len(banId[i]):
            m = len(uid[i])
            for j in range(m):
                if banId[i][j] == '*':
                    continue
                elif banId[i][j] != uid[i][j]:
                    return False
        else:
            return False
    return True
                

def solution(user_id, banned_id):
    n = len(banned_id)
    possUser = permutations(user_id, n)
    
    repo = []
    for u in possUser:
        if isMatch(u, banned_id):
            if set(u) not in repo:
                repo.append(set(u))
    return len(repo)
    
    