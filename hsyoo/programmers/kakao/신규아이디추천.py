def solution(new_id):
    new_id = new_id.lower()
    accept_list= ['-', '_', '.']
    s = ''
    for case in new_id:
        if case.isalnum() or case in accept_list:
            s += case
    while '..' in s:
        s = s.replace('..', '.')
    if len(s) >= 1 and s[0] == '.':
        s = s[1:]
    else:
        pass
    if len(s) >= 1 and s[-1] == '.':
        s = s[:-1]
    else:
        pass
    if len(s) == 0:
        s = 'a'
    if len(s) > 15:
        s = s[:15]
        if s[-1] == '.':
            s = s[:-1]
    if len(s) <= 2:
        s = s + s[-1] * (3 - len(s))
        
        
    return s
print(solution("=.="))