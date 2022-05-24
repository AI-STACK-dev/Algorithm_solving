from copy import deepcopy
def solution(array, commands):
    answer = []
    n = len(commands)
    for cmd in commands:
        i,j,k = cmd
        temp = deepcopy(array[i-1:j])
        temp.sort()
        answer.append(temp[k-1])
    return answer