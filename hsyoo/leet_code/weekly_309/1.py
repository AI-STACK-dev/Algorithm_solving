# 소문자로 이루어진 스트링, 스트링은 두번 반복, 
# 그 두 번 나타난 소문자들의 거리를 체크하면됨. 근데 distance ary에서 idx에 존재하는데
# string안에 값이 없으면 무시해도됨
# for문은 chr을 이용해서 푼다.
# 그 후에는 각각의 위치가 맞는지를 체크해야함. string 내에서 문자가 무조건 두 번 발생
# string의 길이가 짧으므로 index등을 활용해도됨
# index는 제일 먼저 등장하는 경우를 return하기 때문에, reverse 후에 length - idx하면 뒤에서부터 구할 것임
# length - idx(3) : 3 --> -1해줘야함. 뒤에꺼는 length - idx - 1
# 앞에꺼는 idx
class Solution:
    def checkDistances(self, s, distance):
        answer = True
        length = len(s)
        rev_s = s[::-1]
        for index, item in enumerate(distance):
            char_idx = 97 + index
            char = chr(char_idx)
            if char in s:
                start = s.index(char)
                end = length - rev_s.index(char) - 1
                if end - start - 1 == item:
                    continue
                else:
                    answer = False
                    break
            else:
                continue
        return answer
        
print(Solution().checkDistances('abaccb', [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
print(Solution().checkDistances('aa', [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))