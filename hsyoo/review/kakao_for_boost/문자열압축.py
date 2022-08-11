# def solution(s):
#     answer = 0
#     n = len(s)
#     result = []
#     for step in range(1, n //2+ 1):
#         complete = ''
#         count = 1
#         prev = s[:step]
#         prev_pt = step
#         for idx in range(2*step, n, step):
#             if s[prev_pt:idx] == prev:
#                 count += 1
#                 prev_pt = idx
#             else:
#                 # s[prev_pt:idx]가 현재 단어
#                 if count == 1:
#                     complete += prev
#                 else:
#                     complete += str(count) + prev
#                 prev = s[prev_pt:idx]
#                 prev_pt = idx
#                 count = 1
#         # complete = complete + str(count) + s[prev_pt:] if prev == s[prev_pt] else complete + prev
#         cur = s[idx:]
#         if prev == cur:
#             count += 1
#             complete += str(count) + prev
#         else:
#             complete += prev + cur


#         print(step, complete)
#         result.append(len(complete))
#     answer = min(result)
#     return answer

# print(solution('aabbaccc'))
# print(solution('ababcdcdababcdcd'))

def solution(s):
    answer = len(s)
    n = len(s)
    for step in range(1, n//2 + 1):
        complete = ''
        prev = s[:step]
        count = 1
        for j in range(step, n, step):
            if prev == s[j:j+step]:
                count += 1
            else:
                complete += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1
        complete += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(complete))
    return answer

print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))