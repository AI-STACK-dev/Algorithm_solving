from collections import defaultdict

def solution(id_list, reports, k):
    answer = []
    db = defaultdict(set)
    mail_db = defaultdict(int)
    for report in reports:
        from_, to_ = report.split()
        db[to_].add(from_)
    
    for key_ in db.keys():
        if len(db[key_]) >= k:
            for user_id in db[key_]:
                mail_db[user_id] += 1
    for id_ in id_list:
        answer.append(mail_db[id_])
        
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"]	,["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	, 2 ))
print(solution(["con", "ryan"]	, ["ryan con", "ryan con", "ryan con", "ryan con"]	, 3))