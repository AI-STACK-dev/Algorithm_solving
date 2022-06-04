from collections import defaultdict

def solution(id_list, reports, k):
    from_to_dict = defaultdict(set) # 누가 누구를 신고했는지
    to_from_dict = defaultdict(list)# 누가 누구한테서 신고를 받았는지
    count_dict = defaultdict(int)

    for report in reports:
        from_, to_ = report.split()
        from_to_dict[from_].add(to_)
    
    #key_는 신고한사람
    for key_ in from_to_dict.keys():
        for id_ in id_list:
            if id_ in from_to_dict[key_]:
                to_from_dict[id_].append(key_)
    
    for key_ in to_from_dict.keys():
        if len(to_from_dict[key_]) >= k:
            for cnt_key in to_from_dict[key_]:
                count_dict[cnt_key] += 1
    
    answer = []
    for id_ in id_list:
        answer.append(count_dict[id_])
    
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"]	,["ryan con", "ryan con", "ryan con", "ryan con"]	, 3 ))