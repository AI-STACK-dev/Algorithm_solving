from itertools import combinations

def solution(orders, course):
    answer = []
    set_ = set()
    for order in orders:
        set_.update(order)
    cands = list(set_)
    cands.sort()
    for num in course:
        combs = list(combinations(cands, num))
        for comb in combs:
            cnt = 0
            for order in orders:
                flag = True
                for case in comb:
                    flag = flag and (case in order)
                print(f"flag : {flag}, comb : {comb}, order : {order}")
                if flag == True:
                    cnt += 1
            if cnt >= 2:
                answer.append(comb)
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))