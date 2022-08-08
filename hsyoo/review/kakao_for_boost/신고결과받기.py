from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    report_from = defaultdict(set)
    report_to = defaultdict(int)
    for case in report:
        from_, to_ = case.split(' ')
        report_from[to_].add(from_)
    for key_ in report_from.keys():
        if len(report_from[key_]) >= k:
            temp_list = list(report_from[key_])
            for item in temp_list:
                report_to[item] +=1
    for id_ in id_list:
        answer.append(report_to[id_])
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"]	, ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	, 2))
print(solution(["con", "ryan"]	, ["ryan con", "ryan con", "ryan con", "ryan con"]	, 3))