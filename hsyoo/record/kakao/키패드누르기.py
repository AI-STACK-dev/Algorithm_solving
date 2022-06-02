def solution(numbers, hand):
    answer = ''
    pad = {'1': (0,0), '2':(0,1),'3':(0,2),'4':(1,0), '5':(1,1), '6':(1,2), '7':(2,0),
    '8':(2,1), '9':(2,2), '*':(3,0), '0':(3,1), '#':(3,2)}
    left_p, right_p = (3,0), (3,2)
    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            left_p = pad[str(num)]
        elif num in [3,6,9]:
            answer += 'R'
            right_p = pad[str(num)]
        else:
            point = pad[str(num)]
            l_dist = abs(point[0] - left_p[0]) + abs(point[1] - left_p[1])
            r_dist = abs(point[0] - right_p[0]) + abs(point[1] - right_p[1])
            if l_dist < r_dist:
                answer += 'L'
                left_p = point
            elif r_dist < l_dist:
                answer += 'R'
                right_p = point
            else:
                if hand == 'right':
                    answer += 'R'
                    right_p = point
                else:
                    answer += 'L'
                    left_p = point
    return answer
    
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	, 'right'))