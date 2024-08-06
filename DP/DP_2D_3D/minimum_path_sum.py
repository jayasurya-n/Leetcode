from typing import List,Optional
import sys
class Solution:

    # def findPathSum(self,i,j,dp,grid):
    #     if(i<0 or j<0):return sys.maxsize
    #     if(i==0 and j==0):return grid[0][0]

    #     if(dp[i][j]!=-1):return dp[i][j]
    #     dp[i][j] = grid[i][j]+min(self.findPathSum(i-1,j,dp,grid),self.findPathSum(i,j-1,dp,grid))
    #     return dp[i][j]

    # def minPathSum(self, grid: List[List[int]]) -> int:         
    #     i,j = len(grid)-1,len(grid[0])-1
    #     m,n = len(grid),len(grid[0])
    #     dp = [[-1]*n for _ in range(m)]
    #     return self.findPathSum(i,j,dp,grid)

    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m,n = len(grid),len(grid[0])
    #     dp = [[-1]*n for _ in range(m)]

    #     for i in range(0,m):
    #         for j in range(0,n):
    #             if(i==0 and j==0):dp[i][j] = grid[i][j]
    #             elif(i==0):dp[i][j] = grid[i][j]+dp[i][j-1]
    #             elif(j==0):dp[i][j] = grid[i][j]+dp[i-1][j]
    #             else:dp[i][j] = grid[i][j]+min(dp[i-1][j],dp[i][j-1])
    #     print(dp)
    #     return dp[m-1][n-1] 

    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        prev = [sys.maxsize]*n
        prev[0] = 0
        
        for i in range(0,m):
            curr = sys.maxsize
            for j in range(0,n):
                ans = grid[i][j]+min(prev[j],curr)
                prev[j] = ans
                curr = ans
        return prev[n-1]




# time complexity: O(m*n), O(m*n),O(m*n)
# space complexity: O(m*n+(m+n)(stack space)), O(m*n),O(n)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        m,n = list(map(int,input().strip().split()))
        grid = [list(map(int,input().strip().split())) for _ in range(m)]
        print(Solution().minPathSum(grid))