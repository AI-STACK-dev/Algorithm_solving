# *과 #위치에 손가락 존재.
# 싱하좌우로만 움직인다.
# 1, 4, 7 -> 왼손
# 3, 6,8 -> 오른손
# 2,5, 8,0은 기끼은 손가락이 가고 둘다 거리가 가까우면 hand에 따라 진행.
# 왼손과 오른손에 대해 l_y, l_x, r_y, r_x를 적용한다.
# init: l: (3, 0) r: (3,2) /// 그리고 키패드에 대해 dictionary로 위치 저장하기.
# 누르고 난 다음에는 l, r 값ㅇ,ㄹ replace해야함.
# 

def solution(numbers, hand):
    answer = ''
    hash = {'1': (0,0), '2':(0,1), '3':(0,2), '4':(1,0), '5':(1,1), '6':(1,2), '7':(2,0), '8':(2,1), 
    '9':(2,2), '*': (3,0), '0':(3,1), '#':(3,2)}
    l = (3,0)
    r = (3,2)
    for number in numbers:
        if str(number) in '147':
            answer += 'L'
            l = hash[str(number)]
        elif str(number) in '369':
            answer += 'R'
            r = hash[str(number)]
        else:
            coord_y, coord_x = hash[str(number)]
            l_dist = abs(coord_y - l[0]) + abs(coord_x - l[1])
            r_dist = abs(coord_y - r[0]) + abs(coord_x - r[1])
            if l_dist < r_dist:
                answer += 'L'
                l = (coord_y, coord_x)
            elif r_dist < l_dist:
                answer += 'R'
                r = (coord_y, coord_x)
            else:
                if hand == 'left':
                    answer += 'L'
                    l = (coord_y, coord_x)
                else:
                    answer += 'R'
                    r = (coord_y, coord_x)
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	, 'right'))