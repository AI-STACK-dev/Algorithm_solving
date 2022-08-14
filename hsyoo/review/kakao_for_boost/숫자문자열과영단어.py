from collections import defaultdict
def solution(s):
    answer = 0
    hash = {'zero': '0', 'one': '1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7',
            'eight':'8', 'nine':'9'}
    for key_ in hash.keys():
        while key_ in s:
            s = s.replace(key_, hash[key_])
    return int(s)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
