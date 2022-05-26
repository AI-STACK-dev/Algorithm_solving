# def solution(s):
#     set_ = set(list(s))
#     list_ = [chr(i)+chr(i) for i in range(97,123) if chr(i) in set_]
    
#     for temp in list_:
#         while temp in s:
#             s = s.replace(temp, '')
#     if len(s) > 0:
#         return 0
#     else:
#         return 1
def solution(s):
    stack = []
    for case in s:
        if len(stack) == 0:
            stack.append(case)
        elif len(stack) > 0 and stack[-1] == case:
            stack.pop()
        elif len(stack) > 0 and stack[-1] != case:
            stack.append(case)
    if len(stack) == 0:
        return 1
    else:
        return 0
print(solution('cdcd'))
print(solution("baabaa"))
print(solution('abbabb'))