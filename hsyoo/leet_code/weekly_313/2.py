class Solution:
    def maxSum(self, grid):
        answer = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m-2):
            for j in range(n-2):
                temp = 0
                for y in range(3):
                    for x in range(3):
                        temp += grid[i+y][j+x]
                temp = temp - grid[i+1][j] - grid[i+1][j+2] 
                answer = max(answer, temp)
        return answer

print(Solution().maxSum([[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]))
print(Solution().maxSum([[1,2,3],[4,5,6],[7,8,9]]))
        