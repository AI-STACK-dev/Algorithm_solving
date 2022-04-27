from bisect import bisect_left, bisect_right
from itertools import combinations

"""
1차 풀이
-> 효율성 떨어짐
"""
# def solution(info, query):
#     dict_ = {'cpp':0, 'java':1, 'python':2, '-':3}
#     test_idx = []
#     infos = []
#     length_i = 0 
#     idxs_i = []
#     for case in info:
#         lan, sup, exp, dish, score = case.split(' ')
#         infos.append((lan, sup, exp, dish, int(score)))
#         test_idx.append(lan)
#         length_i += 1

#     infos.sort()
#     test_idx.sort()
#     for lan in ['cpp', 'java', 'python']:
#         left = bisect_left(test_idx, lan)
#         right = bisect_right(test_idx, lan)
#         idxs_i.append((left, right))
#     idxs_i.append((0,length_i))

#     result = []
#     for q in query:
#         lan, sup, exp, res = q.split(' and ')
#         dish, score = res.split(' ')
#         start, end = idxs_i[dict_[lan]]
#         cnt = 0
#         for idx in range(start, end):
#             id_ = infos[idx]
#             check1 = True if id_[1] == sup or sup == '-' else False
#             check2 = True if id_[2] == exp or exp == '-' else False
#             check3 = True if id_[3] == dish or dish == '-' else False
#             check4 = True if int(id_[4]) >= int(score) else False
#             if check1 and check2 and check3 and check4:
#                 cnt+=1

#         result.append(cnt)
#     return result

from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(information, queries):
    answer = []
    dic = defaultdict(list)
    for info in information:
        info = info.split()
        condition = info[:-1]  
        score = int(info[-1])
        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                dic[key].append(score) 

    for value in dic.values():
        value.sort()   

    for query in queries:
        query = query.replace("and ", "")
        # print(query)
        query = query.split()
        # print(query)
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        if target_key in dic:
            target_list = dic[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)      
    return answer

    

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
# info = ["java backend junior pizza 150"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# query = ["- and - and - and - 150"]
print(solution(info, query))