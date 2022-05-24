from collections import Counter

def solution(participant, completion):
    answer = ''
    c = Counter(participant)
    for comp in completion:
        c[comp] -= 1
    
    return c.most_common()[0][0]