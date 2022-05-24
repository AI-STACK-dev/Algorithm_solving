def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        temp = str(bin(num1|num2)[2:])
        temp = temp.rjust(n, '0')
        temp = temp.replace('1', '#')
        temp = temp.replace('0', ' ')
        answer.append(temp)
    return answer

print(solution(6,[46, 33, 33 ,22, 31, 50], 	[27 ,56, 19, 14, 14, 10]))