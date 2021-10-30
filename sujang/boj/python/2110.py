from sys import stdin

def binary_serach_spot(array,target):
    start,end = 1,array[-1]-array[0]
    ans = 1
    while start <= end:
        mid = (start + end)//2
        cnt = 1
        compare = array[0]
        for x in array[1:]:
            if x - compare >= mid:
                compare = x
                cnt += 1
        if cnt >= target:
            start = mid + 1
            ans = mid
        else:
            end = mid -1
    return ans 

n,c = map(int,stdin.readline().rstrip().split())
data = [int(stdin.readline().rstrip()) for _ in range(n)]
data.sort()

print(binary_serach_spot(data,c))