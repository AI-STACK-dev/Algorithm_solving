from collections import Counter

def solution(N, stages):
    result = []
    players = len(stages)
    c = Counter(stages)
    for stage in range(1, N+1):
        try:
            rate = c[stage] / players
        except : 
            rate = 0
        result.append((stage, rate))
        players -= c[stage]
    result.sort(key = lambda x : (-x[1], x[0]))
    answer = [x[0] for x in result]
    return answer

print(solution(8, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))