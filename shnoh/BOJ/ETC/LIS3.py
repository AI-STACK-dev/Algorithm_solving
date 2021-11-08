import sys 
import math
def LIS_DP_log(A, n):
    def binary_search(target,left,right): # 이진 탐색
        mid = (left+right) // 2
        middle = DP[mid]
        if middle == target: # 같을 경우, DP를 그대로 유지
            return mid
        if middle < target and target < DP[mid + 1]: # target이 현재 조사하고 있는 위치의 DP 값보다 크고, 다음 위치의 DP 값보다 작다면, 다음 위치의 DP 값을 갱신한다.
            return mid + 1 # DP의 정의가 길이가 k인 부분수열 중 더 작은 수를 저장하는 것이기 때문!
        elif middle < target:
            return binary_search(target,mid+1,right) # 오른쪽 부분 조사
        else:
            return binary_search(target,left,mid - 1) # 왼쪽 부분 조사

    DP = [math.inf] * (n + 1) # DP[k]는 k개의 부분수열 중 최소값
    DP[0] = 0 # DP[1]이 갱신 되도록 하기 위해서, A의 첫수부터 자연스럽게 DP에 저장되도록 하기위함
    cur_k = 0 # 현재 k, 즉 현재까지의 LIS의 길이를 저장하는 변수
    for num in A: # A를 순회하며
        if DP[cur_k] < num: # k가 1 증가하는 경우: 현재까지 저장된 수보다 크므로 LIS 만족
            cur_k += 1 # k + 1
            DP[cur_k] = num # 증가한 k에 맞춰 현재 수를 DP에 저장
        else: # LIS의 길이를 늘리지 못하는 경우, 이전 값들을 최적화. 즉, DP[k]가 LIS k길이의 최소값이도록 갱신
            DP[binary_search(num, 0, cur_k)] = num # DP가 오름차순이 되므로, 이진 탐색(logn)으로 갱신할 위치를 찾는다.
    return cur_k # A를 마지막까지 순회했을 때의 k: 현재까지의 LIS의 길이
 
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
print(LIS_DP_log(A,n))