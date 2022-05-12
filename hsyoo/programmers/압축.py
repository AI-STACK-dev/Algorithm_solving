from collections import defaultdict

def solution(msg):
    answer = []
    dict_ = {}
    dict_idx = 1
    for i in range(65, 91):
        dict_[chr(i)] = dict_idx
        dict_idx += 1
    start = 0
    end = 0
    n = len(msg)
    while True:
        end += 1
        if end == n:
            answer.append(dict_[msg[start:end]])
            break
        if msg[start:end+1] not in dict_:
            dict_[msg[start:end+1]] = len(dict_) + 1
            answer.append(dict_[msg[start:end]])
            start = end

    return answer

print(solution("TOBEORNOTTOBEORTOBEORNOT"))