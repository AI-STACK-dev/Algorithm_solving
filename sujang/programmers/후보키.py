from itertools import combinations

def solution(r):
    n = len(r[0])
    demoList = list(range(n))
    ans = []
    for i in range(1, n+1):
        for li in combinations(demoList,i):
            tempDict = {}
            for row in r:
                tempStr = ""
                for idx in li:
                    tempStr += row[idx]
                if tempStr in tempDict:
                    break
                tempDict[tempStr] = 1
            else:
                for a in ans:
                    if set(a).issubset(li):
                        break
                else:
                    ans.append(set(li))
    return len(ans)
    

a = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(a))

