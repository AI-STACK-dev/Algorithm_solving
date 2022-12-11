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
        print(temp_c)
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

from collections import deque


def bfs(n, info):
    result = []
    q = deque([(0, [0,0,0,0,0,0,0,0,0,0,0])])
    max_gap = 0

    while q:
        focus, arrow = q.popleft()
        if sum(arrow) == n:
            apch, ryan = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] > arrow[i]:
                        apch += (10 - i)
                    else:
                        ryan += (10 - i)
            if ryan > apch:
                gap = ryan - apch
                if max_gap > gap:
                    continue
                if gap > max_gap:
                    max_gap = gap
                    result.clear()
                result.append(arrow)
        elif sum(arrow) > n:
            continue
        elif focus == 10:
            temp = arrow.copy()
            temp[focus] = n - sum(temp)
            q.append((-1, temp))
        else:
            temp = arrow.copy()
            temp[focus] = info[focus] + 1
            q.append((focus + 1, temp))

            temp2 = arrow.copy()
            temp2[focus] = 0
            q.append((focus + 1, temp2))

    return result


def solution(n, info):
    win_list = bfs(n, info)

    if not win_list:
        return [-1]
    elif len(win_list) == 1:
        return win_list[0]
    else:
        return win_list[-1]
print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]	))