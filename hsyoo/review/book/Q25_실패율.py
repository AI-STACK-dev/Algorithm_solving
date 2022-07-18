def solution(N, stages):
    answer = []
    length = len(stages)
    for i in range(1, N +1):
        count = stages.count(i)
        if length == 0:
            error = 0
        else:
            error = count / length
        answer.append((i, error))
        length -= count
    answer = sorted(answer, key = lambda x : x[1], reverse = True)
    answer = [i[0] for i in answer]
        
        

    return answer