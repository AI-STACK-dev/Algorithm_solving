def solution(new_id):
    checking = ['-', '_', '.']
    new_id = new_id.lower()
    s = ''
    for case in new_id:
        if case.isalnum() or case in checking:
           s += case
    while '..' in s:
        s= s.replace('..', '.') 
    if len(s) > 0 and s[0] == '.':
        s = s[1:]
    if len(s) > 0 and s[-1] == '.':
        s = s[:-1]
    if len(s) == 0:
        s = 'a'
    if len(s) > 15:
        s = s[:15]
        if s[-1] == '.':
            s = s[:-1]
    if len(s) < 3:
        s = s + (s[-1] * (3 - len(s)))
    return s

# print(solution("...!@BaT#*..y.abcdefghijklm"	))
print(solution("z-+.^."	))
# print(solution("=.="	))
# print(solution("123_.def"	))
# print(solution("abcdefghijklmn.p"	))
    
