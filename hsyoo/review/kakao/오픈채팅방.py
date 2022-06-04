from collections import defaultdict

def solution(records):
    answer = []
    db = defaultdict(str)
    for record in records:
        log = record.split()
        if len(log) == 3:
            db[log[1]] = log[2]
    
    for record in records:
        log = record.split()
        if log[0] == 'Enter':
            answer.append(f"{db[log[1]]}님이 들어왔습니다.")
        elif log[0] == 'Leave':
            answer.append(f"{db[log[1]]}님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	))