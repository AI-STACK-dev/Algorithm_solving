from collections import defaultdict

def solution(s):
    dict = {}
    code = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        dict[code[i]] = i
    
    result = ''
    eng = ''
    for i in s:
        if i.isdigit():
            result = result+i
        elif i.isalpha():
            eng = eng+i
            if eng in dict.keys():
                result = result + str(dict[eng])
                eng=''
    return int(result)

def solution2(s):
    en = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''
    for idx, num in enumerate(en):
        if num in s:
            s = s.replace(num, str(idx))
        answer=s
    return int(answer)
print(solution("one4seveneight"))
print(solution2("one4seveneight"))