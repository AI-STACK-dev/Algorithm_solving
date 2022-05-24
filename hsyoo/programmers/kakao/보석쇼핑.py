from collections import defaultdict

def solution(gems):
    start, end = 0,0
    min_ = len(gems) + 1
    check_len = len(set(gems))
    dict_ = defaultdict(int)
    while end < len(gems):
        dict_[gems[end]] += 1
        end += 1
        if len(dict_) == check_len:
            while start < end:
                if dict_[gems[start]] > 1:
                    dict_[gems[start]] -= 1
                    start += 1
                elif end - start < min_:
                    min_ = end - start
                    answer = [start+1, end]
                    break
                else:
                    break
            
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
# a = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
# a = ['ruby', 'ruby','ruby','ruby','dia','ruby','ruby','ruby','ruby']
# a = ['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'b', 'c', 'a']
# a = ["A","A","A","B","B"]
# a = ["A"]
# a = ["A","B","B","B","B","B","B","C","B","A"]
# print(solution(a))
