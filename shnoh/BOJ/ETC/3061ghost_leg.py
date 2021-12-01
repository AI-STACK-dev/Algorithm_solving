import sys
input = sys.stdin.readline

def bubbleSort(A):
    global N
    count = 0
    for i in range(N):
        for j in range(N - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                count += 1
    return count

T = int(input())
for _ in range(T):
    N = int(input())
    data = [int(x) for x in input().split()]
    print(bubbleSort(data))

#print(data)

