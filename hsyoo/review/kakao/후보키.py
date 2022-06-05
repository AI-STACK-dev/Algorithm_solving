# from itertools import combinations

# def solution(relation):
#     answer = 0
#     n = len(relation)
#     m = len(relation[0])

#     set_list = []
#     for k in range(0, m):
#         combs = combinations(range(m), k+1)
#         for comb in combs:
#             flag = True
#             for case in set_list:
#                 if set(comb).issubset(case):
#                     flag = False
#             if flag == False:
#                 continue
#             comb_set = set()
#             for i in range(n):
#                 temp = []
#                 for j in range(k+1):
#                     temp.append(relation[i][comb[j]])
#                 comb_set.update(temp)
#             if len(comb_set) == n:
#                 set_list.append(comb_set)
#             else:
#                 continue
#     # print(comb_set)
#     answer = len(set_list)
#     return answer

from itertools import combinations

def solution(relation):
    n = len(relation)
    m = len(relation[0])

    comb = []
    for i in range(1, m+1):
        comb.extend(combinations(range(m), i))
    
    set_list = []
    for case in comb:
        temp = [tuple([item[key] for key in case]) for item in relation]
        print(temp)
        if len(set(temp)) == n:
            flag = True
            for set_ in set_list:
                if set(set_).issubset(set(case)):
                    flag = False
                    break
            if flag == True:
                set_list.append(case)
            
    return len(set_list)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]	))