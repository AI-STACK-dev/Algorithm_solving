def solution(record):
    answer = []
    dict_ = {}
    for log in record:
        print(log)
        if log.count(' ') == 2:
            cmd, id_, nickname= log.split(' ')
        else:
            cmd, id_ = log.split(' ')
        if dict_.get(id_) == None:
            new = nickname
            dict_[id_] = new
        else:
            old = dict_[id_]
            new = nickname
            dict_[id_] = new
            for ans in answer:
                ans.replace(old, new)
        if cmd == 'Enter':
            str_ = f"{new}님이 들어왔습니다."
            answer.append(str_)
        elif cmd == 'Leave':
            str_ = f"{new}님이 나갔습니다."
            answer.append(str_)
        elif cmd == 'Change':
            old = dict_[id_]
            new = nickname
            dict_[id_] = new
            for ans in answer:
                ans.replace(old, new)
            
        
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))