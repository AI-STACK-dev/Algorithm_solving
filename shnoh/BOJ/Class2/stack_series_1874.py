import sys

def solve(n,target): # 입력 수열
    stack = [] # 뽑아서 저장해두는 스택
    push_pop_list = [] # + - 로 이루어진 리스트(출력용)
    num = 1 # 현재 오름차순으로 어느 수까지 push했는지
    for i in range(n): 
        while num <= target[i]:
            stack.append(num)
            push_pop_list.append("+")
            num += 1
        if stack[-1] == target[i]:
            stack.pop()
            push_pop_list.append("-")
        else:
            print("NO")
            return
    for pm in push_pop_list: # plus minus
        print(pm)
    return

n = int(sys.stdin.readline())
target = [int(sys.stdin.readline()) for _ in range(n)]
solve(n,target)

    # num = 1 # 현재 오름차순으로 어느 수까지 push했는지
    # temp_stack = [] # 임시로 넣어둘 스택
    # maken_stack = [] # 뽑아서 만들 스택
    # push_pop_stack = [] # + - 로 이루어진 리스트(출력용)

    # # 초기값 설정. 
    # for i in range(target[0]): 
    #     temp_stack.append(num)
    #     push_pop_stack.append("+")
    #     num += 1
    # maken_stack.append(temp_stack.pop())
    # push_pop_stack.append("-")
    # # 본격 스택 만들어지는지 확인하는 부분
    # for i in range(1, n): 
    #     if not temp_stack: # 빼 둔게 없으면. 새로 넣어야지...

    #     if temp_stack[-1] == target[i]: # 스택에서 연속적으로 넣는 경우
    #         maken_stack.append(temp_stack.pop())
    #         push_pop_stack.append("-")
    #     elif num > n: # 만들 수 없다. 더 이상 조작이 불가능한데, 원하는 수열을 만들 수 없기때문
    #         print("NO")
    #         return
    #     else: # 다시 temp 스택에서 임시로 넣어줄 필요가 있을 때
    #         while num <= target[i]:
    #             temp_stack.append(num)
    #             push_pop_stack.append("+")
    #             num += 1
    #         maken_stack.append(temp_stack.pop())
    #         push_pop_stack.append("-")
    # for pm in push_pop_stack: # plus minus
    #     print(pm)
    # return


    
