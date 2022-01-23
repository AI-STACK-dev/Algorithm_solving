'''
문제 1.
17분 28초 소요
'''
def solution(id_list, report, k):
    # 신고 받은 유저 정요
    sued_dict = {}
    for string in report:
        a,b = string.split()
        if b in sued_dict.keys():
            if not a in sued_dict[b]:
                sued_dict[b].append(a)
        else:
            sued_dict[b] = [a]
            
    # 유저들의 상태 업데이트
    answer = [0]*len(id_list)
    for string in sued_dict.keys():
        if len(sued_dict[string]) >= k:
            for name in sued_dict[string]:
                answer[id_list.index(name)] += 1
    return answer