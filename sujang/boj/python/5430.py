import sys ; input = sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
    cmds = input().rstrip()
    n = int(input().rstrip())
    String = input().rstrip()
    array = deque(String.lstrip('[').rstrip(']').split(','))
    
    rev = front = 0
    back = len(array)-1
    flag = True

    # 아무것도 없는 입력 예외 처리
    if n ==0:
        array = []
        back = 0

    for c in cmds:
        if c =='R':
            rev += 1
        else:
            if len(array) < 1:
                print("error")
                flag = False
                break
            else:
                if rev % 2 ==0:
                    array.popleft()
                else:
                    array.pop()

    if flag:
        if rev % 2 != 0:
            array.reverse()
        print('[',end='')
        print(*array,sep=',',end=']\n')
    

