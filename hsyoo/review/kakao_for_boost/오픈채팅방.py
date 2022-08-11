from collections import defaultdict

def solution(records):
    answer = []
    hash = defaultdict(str)
    for record in records:
        cmd = record.split(' ')
        if len(cmd) == 3:
            hash[cmd[1]] = cmd[2]
    
    for record in records:
        log = record.split(' ')
        if len(log) == 3:
            cmd, uid, name = log
        else:
            cmd, uid = log
        if cmd == 'Enter':
            answer.append(f"{hash[uid]}님이 들어왔습니다.")
        elif cmd == 'Leave':
            answer.append(f"{hash[uid]}님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	))