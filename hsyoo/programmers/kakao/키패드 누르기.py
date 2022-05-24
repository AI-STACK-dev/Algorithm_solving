def solution(numbers, hand):
    answer = ''
    dict_ = {'1': (0,0), '2': (0,1), '3':(0,2), '4':(1,0), '5': (1,1), '6':(1,2), 
            '7':(2,0), '8':(2,1), '9':(2,2), '*':(3,0), '0':(3,1), '#':(3,2)}
    left_i, left_j, right_i, right_j = 3, 0, 3, 2
    left = [1,4,7]
    right = [3,6,9]
    for num in numbers:
        if num in left:
            answer += 'L'
            left_i, left_j = dict_[str(num)]
        elif num in right:
            answer += 'R'
            right_i, right_j = dict_[str(num)]
        else:
            y, x = dict_[str(num)]
            left_dist = abs(left_i - y) + abs(left_j - x)
            right_dist = abs(right_i - y) + abs(right_j - x)
            if left_dist == right_dist:
                if hand == "left":
                    answer+='L'
                    left_i, left_j = y,x
                else:
                    answer+='R'
                    right_i, right_j = y,x
            elif left_dist < right_dist:
                answer+='L'
                left_i, left_j = y,x
            else:
                answer+='R'
                right_i, right_j = y,x
    print(answer)
    return answer