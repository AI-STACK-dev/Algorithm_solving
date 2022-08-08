def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    check = ['-', '_', '.']
    s = ''
    for case in new_id:
        if case.isalnum() or case in check:
            s += case
    while '..' in s:
        s = s.replace('..', '.')
    if len(s) > 0 and s[0] == '.':
        s = s[1:]
    if len(s) > 0 and s[-1] == '.':
        s = s[:-1]
    if len(s) == 0:
        s = 'a'
    if len(s) >= 16:
        s = s[:15]
        if s[0] == '.':
            s = s[1:]
        if s[-1] == '.':
            s = s[:-1]
    if len(s) <= 2:
        tmp = 3 - len(s)
        s = s + s[-1] * tmp
    answer = s
    return answer

# print(solution("...!@BaT#*..y.abcdefghijklm"	))
# print(solution("z-+.^."	))
# print(solution("=.="	))
# print(solution("123_.def"	))
print(solution("abcdefghijklmn.p"	))