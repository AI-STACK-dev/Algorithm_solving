import sys; input = sys.stdin.readline;
n = int(input())
operands = [int(x) for x in input().split()]
plus, minus, mul, div = map(int, input().split())
Min = 1e9
Max = -1e9
def DFS_Search(i, num):
    global plus, minus, mul, div, Min, Max
    if i == n:
        Min = min(Min, num)
        Max = max(Max, num)
    else:
        if plus > 0:
            plus -= 1
            DFS_Search(i + 1, num + operands[i])
            plus += 1
        if minus > 0:
            minus -= 1
            DFS_Search(i + 1, num - operands[i])
            minus += 1
        if mul > 0:
            mul -= 1
            DFS_Search(i + 1, num * operands[i])
            mul += 1
        if div > 0:
            div -= 1
            DFS_Search(i + 1, int(num / operands[i]))
            div += 1
    
DFS_Search(1, operands[0])
print(Max)
print(Min)