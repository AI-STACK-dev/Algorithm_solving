from itertools import combinations
from collections import Counter

# def solution(orders, course):
#     answer = []
#     set_ = set()
#     for order in orders:
#         set_.update(order)
#     cands = list(set_)
#     cands.sort()
#     for num in course:
#         combs = list(combinations(cands, num))
#         for comb in combs:
#             cnt = 0
#             for order in orders:
#                 flag = True
#                 for case in comb:
#                     flag = flag and (case in order)
#                 print(f"flag : {flag}, comb : {comb}, order : {order}")
#                 if flag == True:
#                     cnt += 1
#             if cnt >= 2:
#                 answer.append(comb)
#     return answer

def solution(orders, course):
    answer = []
    for k in course:
        cands = []
        for menu_list in orders:
            for list_ in combinations(menu_list, k):
                s = ''.join(sorted(list_))
                cands.append(s)
        sorted_cands = Counter(cands).most_common()

        # course 반복문안에 존재하기에 각 글자수 중에서 최빈값들이 매치돼서 answer에 추가된다.
        for menu, cnt in sorted_cands:
            if cnt > 1 and cnt == sorted_cands[0][1]: 
                answer.append(menu)
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))