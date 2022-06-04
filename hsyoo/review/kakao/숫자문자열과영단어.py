def solution(s):
    encode = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    for key_ in encode.keys():
        s = s.replace(key_, str(encode[key_]))
    return int(s)

print(solution("one4seveneight"	))
print(solution("23four5six7"))