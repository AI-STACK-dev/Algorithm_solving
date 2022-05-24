from collections import Counter
from itertools import combinations
"""
1차 풀이
"""
# def solution(orders, course):
#     c_list = []
#     for order in orders:
#         temp = list(order)
#         temp.sort()
#         for i in range(2, len(order)+1):
#             comb = combinations(temp, i)
#             for case in comb:
#                 c_string = ''.join(case)
#                 c_list.append(c_string)
#     c = Counter(c_list)
#     print(c)
#     result = []
#     most_ = c.most_common()
#     most_.sort(key = lambda x : len(x[0]))
#     for cnt in course:
#         max_ = 0
#         for case in most_:
#             alpha_, value = case
#             if len(alpha_) == cnt and value >= max_ and value >= 2:
#                 max_ = value
#                 result.append(alpha_)

#     return sorted(result)

"""
다른 사람 풀이
"""
from itertools import combinations
from collections import Counter

def solution(orders, course):
	answer = []
	for k in course:
		candidates = []
		for menu_li in orders:
			for li in combinations(menu_li, k):
				res = ''.join(sorted(li))
				candidates.append(res)
		sorted_candidates = Counter(candidates).most_common()
		print(sorted_candidates)
		answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
	return sorted(answer)
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
