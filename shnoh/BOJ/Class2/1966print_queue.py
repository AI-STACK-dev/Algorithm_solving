import sys; input = sys.stdin.readline;
from collections import deque, Counter
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    data = [(int(x),i) for i, x in enumerate(input().split())]
    #print(data)
    #counter = Counter(data)
    # counter = [0] * 10
    # for num in data:
    #     counter[num] += 1
    queue = deque(data)
    #print(queue)
    while queue:
        k = queue.popleft()
        # print("k : ", k)
        check = False
        for num, _ in queue:
            if k[0] < num:
                queue.append(k)
                check = True
                # print("check")
                break
        if not check and k[1] == m:
            # print("out!")
            break
    # print("n:",n)
    # print("len:",len(queue))
    count = n - len(queue)
    print(count)
    # 결국 중요도가 높은 것부터 인쇄가 된다.
    # 중요도가 같을 때는? 시뮬레이션을 해봐야...
