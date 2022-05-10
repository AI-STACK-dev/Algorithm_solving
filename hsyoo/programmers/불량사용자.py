from collections import defaultdict
from itertools import combinations, product

def solution(user_id, banned_id):
    user_dict = defaultdict(set)
    count = defaultdict(int)

    for user in user_id:
        n = len(user)
        for r in range(1, n+1):
            combs = combinations(range(n), r)
            for comb in combs:
                temp = list(user)
                for v in comb:
                    temp[v] = '*'
                user_dict[''.join(temp)].add(user)
    # print(user_dict)
    list_ = []
    for ban in banned_id:
        list_.append(list(user_dict[ban]))
    items = list(product(*list_))
    for case in items:
        case = list(case)
        case.sort()
        set_ = set(case)
        if len(set_) != len(banned_id):
            continue
        else:
            set_ = list(set_)
            count['_'.join(set_)]

    answer = len(count.keys())
    return answer
        
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]	))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"]	, ["*rodo", "*rodo", "******"]	))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"]	, ["fr*d*", "*rodo", "******", "******"]	))