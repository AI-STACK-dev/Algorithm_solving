# from itertools import permutations

# def operation(num1, num2, op):
#     if op == '+':
#         return str(int(num1) + int(num2))
#     if op == '-':
#         return str(int(num1) - int(num2))
#     if op == '*':
#         return str(int(num1) * int(num2))

# def calculate(exp, op):
#     print(op)
#     array = []
#     tmp = ''
#     for i in exp:
#         if i.isdigit():
#             tmp += i
#         else:
#             array.append(tmp)
#             array.append(i)
#             tmp = ''
#     array.append(tmp)

#     for o in op:
#         stack = []
#         while len(array) != 0:
#             tmp = array.pop(0)
#             if tmp == o:
#                 stack.append(operation(stack.pop(), array.pop(0), o))
#             else:
#                 stack.append(tmp)
#             print(array, stack)
#         array = stack
#     return abs(int(array[0]))


# def solution(expression):
#     op = ['+', '-', '*']
#     op = list(permutations(op, 3))
#     result=[]
#     for i in op:
#         result.append(calculate(expression, i))
#         break
#     return max(result)

# print(solution("100-200*300-500+20"))

from itertools import permutations
from collections import deque
def operation(num1, num2, op):
    if op == '+':
        return int(num1) + int(num2)
    elif op == '-':
        return int(num1) - int(num2)
    elif op == '*':
        return int(num1) * int(num2)
    
def matching(list_, permute):
    queue = deque(list_)
    print(permute)
    for op in permute:
        stack = []
        while queue:
            print(queue, stack)
            case = queue.popleft()
            if case == op:
                stack.append(operation(stack.pop(), queue.popleft(), op))
            else:
                stack.append(case)
        queue = deque(stack)

    return abs(int(stack[-1]))
    

def solution(expression):
    list_ = []
    ops = []
    temp = ''
    for case in expression:
        if case.isdigit():
            temp += case
        else:
            list_.append(temp)
            temp = ''
            list_.append(case)
    list_.append(temp)
            
    permutes = permutations(['+', '-', '*'], 3)
    results = []
    for permute in permutes:
        results.append(matching(list_, permute))
    
    return max(results)

print(solution("100-200*300-500+20"))