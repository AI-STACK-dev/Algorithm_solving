import sys
k, n = map(int, sys.stdin.readline().split())
A = [int(sys.stdin.readline()) for _ in range(k)]

start = 1 # 길이 시작 지점, 최소값
end = max(A) # 길이 최대값
while start <= end: # 랜선의 길이 이진 탐색
    mid = (start + end) // 2
    cur_n = 0
    for k_len in A:
        cur_n += k_len // mid
    if cur_n >= n: # 만들 수 있으므로, 더 큰 최대 길이를 찾으로 간다.
        start = mid + 1 # 더 큰 길이 범위 탐색
    else:
        end = mid - 1 # n개 만들 수 없으므로, 더 작은 범위 탐색
    # mid가 딱 맞는 경우에도, mid + 1범위부터 탐색하고, 마지막에 end = mid -1 되서 돌아온다.
print(end)