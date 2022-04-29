from collections import defaultdict

def genSubset(List, string, n, N, result):
    if n == N:
        return
    string += List[n]
    result.add(string)
    genSubset(List, string, n+1, N, result)
    string = string[:-1]
    result.add(string)
    genSubset(List, string, n+1, N, result)
    return result

def solution(orders, course):
    n = len(orders)
    
    # 모든 경우의 수 저장
    repo = []
    for i in range(n):
        temp = list(orders[i])
        temp.sort()
        repo.append(genSubset(temp, "", 0, len(temp), set()))

    # dict에 저장
    repoDict = defaultdict(int)
    repoCntDict = defaultdict(int)
    for i in range(n-1):
        for j in range(i+1,n):
            tempSet = repo[i] & repo[j]
            for s in tempSet:
                cnt = len(s)
                repoDict[s] += 1 
                repoCntDict[cnt] = max(repoCntDict[cnt], repoDict[s])
    # 결과 반환
    ans = []
    for k in repoDict.keys():
        if len(k) in course and repoCntDict[len(k)] == repoDict[k]:
            ans.append(k)
    ans.sort()
    return ans
        