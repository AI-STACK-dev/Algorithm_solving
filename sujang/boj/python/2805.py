from sys import stdin

n,m = map(int,stdin.readline().rstrip().split())
data = list(map(int,stdin.readline().rstrip().split()))

def binary_search(target):
    start = 1
    end = max(data)

    ans = 0
    while start <= end:
        mid = (start+end)//2
        sum = 0
        for d in data:
            if d > mid:
                sum += d-mid
        if sum < target:
            end = mid -1
        else:
            ans = mid
            start = mid +1
    return ans
    
print(binary_search(m))