from collections import Counter
from itertools import combinations_with_replacement
import copy
def solution(n, info):
    answer = ''
    comb_list = list(combinations_with_replacement(range(11), n))
    max_counter = None
    max_ = -int(1e9)
    for comb in comb_list:
        temp_c = Counter(comb)
        apch = 0
        ryan = 0
        for i in range(11):
            if temp_c[i] > 0 or info[i] > 0:
                if temp_c[i] > info[i]:
                    ryan += (10 - i)
                elif temp_c[i] <= info[i]:
                    apch += (10 - i)
        diff = abs(ryan - apch)
        if ryan > apch and diff >= max_:
            # print(apch, ryan)
            if max_counter == None:
                max_ = diff
                max_counter = copy.deepcopy(temp_c)
            else:
                if diff == max_:
                    for j in range(11, -1, -1):
                        if temp_c[j] == max_counter[j]:
                            continue
                        elif temp_c[j] > max_counter[j]:
                            max_counter = copy.deepcopy(temp_c)        
                            break
                        else:
                            break
                else:
                    max_ = diff
                    max_counter = copy.deepcopy(temp_c)
    ans = []
    # print(max_counter)
    if max_counter == None:
        return [-1]
    else:
        for i in range(11):
            ans.append(max_counter[i])
    return ans
print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))