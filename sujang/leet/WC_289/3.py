class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m = len(grid); n = len(grid[0])
        
        # util
        def count2and5(num):
            a, b = 0, 0
            while num % 2 == 0:
                num //= 2
                a += 1
            while num % 5 == 0:
                num //= 5
                b += 1
            return [a, b]

        # preprocess
        horiz = [[[0, 0] for _ in range(n)] for _ in range(m)]
        verti = [[[0, 0] for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j == 0:
                    horiz[i][j] = count2and5(grid[i][j])
                else:
                    a,b = count2and5(grid[i][j])
                    horiz[i][j][0] = horiz[i][j-1][0] + a
                    horiz[i][j][1] = horiz[i][j-1][1] + b
        for j in range(n):
            for i in range(m):
                if i == 0:
                    verti[i][j] = count2and5(grid[i][j])
                else:
                    a,b = count2and5(grid[i][j])
                    verti[i][j][0] = verti[i-1][j][0] + a
                    verti[i][j][1] = verti[i-1][j][1] + b
        
        # search
        ans = 0
        for i in range(m):
            for j in range(n):
                a, b = verti[m - 1][j]
                d, e= horiz[i][n - 1]
                x, y = count2and5(grid[i][j])
                a1, b1 = verti[i][j]
                a2, b2= horiz[i][j]
                tmp = [a1 + a2 - x, b1 + b2 - y]
                ans = max(ans, min(tmp))
                tmp = [d - a2 + a1, e - b2 + b1]
                ans = max(ans, min(tmp))             
                tmp = [a - a1 + a2, b - b1 + b2]
                ans = max(ans, min(tmp))
                tmp = [a + d - a1 - a2 + x, b + e - b1 - b2 + y]
                ans = max(ans, min(tmp))
        return ans

        