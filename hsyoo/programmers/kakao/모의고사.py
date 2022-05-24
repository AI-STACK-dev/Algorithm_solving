from collections import Counter

def solution(answers):
    n = len(answers)
    div = n * 2 // 10
    
    ans1 = [1,2,3,4,5,1,2,3,4,5] * (div+1)
    ans2 = [2,1,2,3,2,4,2,5] * (div+1)
    ans3 = [3,3,1,1,2,2,4,4,5,5] * (div+1)
    dict_ = {'1' : ans1, '2':ans2, '3':ans3}
    result = {'1':0, '2':0, '3':0}
    for i in range(n):
        for j in range(1,4):
            if dict_[str(j)][i] == answers[i]:
                result[str(j)] +=1
    print(result)
    c = Counter(result)
    max_ = c.most_common(1)[0][1]
    sol = []
    for i in range(1,4):
        if c[str(i)] == max_:
            sol.append(i)
        
    return sol