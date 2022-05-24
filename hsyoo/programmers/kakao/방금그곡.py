def solution(m, musicinfos):
    # answer = ''
    dict_ = {'C#':'0', 'D#':'1', 'F#':'2', 'G#':'3', 'A#':'4', 'C':'5', 'D':'6', 'E':'7', 'F':'8'
                , 'G':'9', 'A':'a', 'B':'b'}
    for key_ in dict_.keys():
        m = m.replace(key_, dict_[key_])
    # print(f" m : {m}")
    m_infos = []
    for i in range(len(musicinfos)):
        temp = list(musicinfos[i].split(','))
        m_infos.append(temp)
    
    result = []
    for idx, case in enumerate(m_infos):
        minute = 0
        for key_ in dict_.keys():
            case[3] = case[3].replace(key_, dict_[key_])
        h1, m1 = case[0].split(':')
        h2, m2 = case[1].split(':')

        h = int(h2) - int(h1)
        if h > 0:
            minute += h * 60
        if int(m2) - int(m1) > 0:
            minute += (int(m2) - int(m1))
        elif int(m2) - int(m1) < 0:
            minute -= abs(int(m2) - int(m1))
        
        mul = minute // len(case[3])
        res = minute % len(case[3])
        temp_music = case[3] * mul + case[3][:res]
        if m in temp_music:
            result.append([case[2], minute, idx])
    if len(result) == 1:
        answer = result[0][0]
    elif len(result) == 0:
        answer = "(None)"
    else:
        result.sort(key = lambda x : [-x[1], x[2]])
        answer = result[0][0]
    # print(result)
    return answer

m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# m = "CC#BCC#BCC#BCC#B"
# musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
m = "ABC"
musicinfos = 	["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))