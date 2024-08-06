from typing import List,Optional
import sys
class Solution:

    # def findPaths(self,i,j,dp,grid):
    #     if(i<0 or j<0):return 0
    #     if(grid[i][j]==1):return 0
    #     if(i==0 and j==0):return 1

    #     if(dp[i][j]!=-1):return dp[i][j]
    #     dp[i][j] = self.findPaths(i-1,j,dp,grid)+self.findPaths(i,j-1,dp,grid)
    #     return dp[i][j]


    # def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:              
    #     i,j = len(grid)-1,len(grid[0])-1
    #     m,n = len(grid),len(grid[0])
    #     dp = [[-1]*n for _ in range(m)]
    #     return self.findPaths(i,j,dp,grid)

    # def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
    #     m,n = len(grid),len(grid[0])
    #     dp = [[-1]*n for _ in range(m)]

    #     dp[0][0] = 1 if(grid[0][0]==0) else 0
    #     for i in range(1,m):
    #         if(grid[i][0]==1 or dp[i-1][0]==0):dp[i][0] = 0
    #         else:dp[i][0] = 1

    #     for j in range(1,n):
    #         if(grid[0][j]==1 or dp[0][j-1]==0):dp[0][j] = 0
    #         else:dp[0][j] = 1

    #     for i in range(1,m):
    #         for j in range(1,n):
    #             if(grid[i][j]==1):dp[i][j] = 0
    #             else:
    #                 dp[i][j] = dp[i-1][j]+dp[i][j-1]
    #     return dp[m-1][n-1] 

    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        prevRow = [-1]*n
        prevRow[0] = 1 if(grid[0][0]==0) else 0
        for j in range(1,n):
            if(grid[0][j]==1 or prevRow[j-1]==0):prevRow[j] = 0
            else:prevRow[j] = 1

        prevColumn = [-1]*m
        prevColumn[0] = 1 if(grid[0][0]==0) else 0
        for i in range(1,m):
            if(grid[i][0]==1 or prevColumn[i-1]==0):prevColumn[i] = 0
            else:prevColumn[i] = 1

        if(n==1):return prevColumn[m-1]
        if(m==1):return prevRow[n-1]

        for i in range(1,m):
            prevValue = prevColumn[i]
            for j in range(1,n):
                if(grid[i][j]==1):ans = 0
                else:ans = prevRow[j]+prevValue
                prevValue = ans
                prevRow[j] = ans
        return prevRow[n-1]



# time complexity: O(m*n), O(m*n),O(m*n)
# space complexity: O(m*n+(m+n)(stack space)), O(m*n),O(m+n)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        m,n = list(map(int,input().strip().split()))
        grid = [list(map(int,input().strip().split())) for _ in range(m)]
        print(Solution().uniquePathsWithObstacles(grid))