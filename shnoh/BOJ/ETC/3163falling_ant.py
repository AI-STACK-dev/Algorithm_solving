import sys
from collections import deque

T = int(sys.stdin.readline())
for i in range(T):
    N, L, k = map(int, input().split())
    Id_List = [] # 아이디들의 리스트 몊번째 떨어진 아이디인지 조사하기 위함.
    Left = [] # 왼쪽으로 떨어지는 데 시간 리스트
    right = [] # 오른쪽으로 떨어지는 데 시간 리스트
    for _ in range(N):
        loc, Id = map(int, input().split())
        if Id > 0: # 양수 오른쪽으로 이동
            right.append(L - loc) # 작은 수가 마지막에 옴
        else:
            Left.append(loc) # 큰 수가 마지막에 옴
        Id_List.append(Id)
    
    Left.reverse() # 내림차순으로 만들어주기 위함. pop().즉, O(1)로 사용하기 위해서
    Id_List_deque = deque(Id_List) # 앞뒤(왼쪽, 오른쪽)로 빼야 하므로 deque! O(1)로 pop() 안하면 시간초과.

    cur_k = 0 # 현재 떨어진 개수
    Last_Id = 0 # 마지막으로 떨어진 아이디
    while cur_k < k:
        if not Left: # 왼쪽이 떨어진 경우
            right.pop()
            Last_Id = Id_List_deque.pop()
        elif not right: # 오른쪽이 다 떨어진 경우
            Left.pop()
            Last_Id = Id_List_deque.popleft()
        else:
            if Left[-1] == right[-1]: # 양쪽에서 같이 떨어지는 경우
                if Id_List_deque[0] < Id_List_deque[-1]: # Id가 더 작은 것을 먼저 뺀다!
                    Left.pop()
                    Last_Id = Id_List_deque.popleft()
                else:
                    right.pop()
                    Last_Id = Id_List_deque.pop()
            elif Left[-1] < right[-1]: # 현재 있는 것 중, 왼쪽이 먼저 떨어지는 경우
                Left.pop()
                Last_Id = Id_List_deque.popleft()
            else: # 현재 있는 것 중, 오른쪽이 먼저 떨어지는 경우
                right.pop()
                Last_Id = Id_List_deque.pop()
        cur_k += 1
    print(Last_Id)