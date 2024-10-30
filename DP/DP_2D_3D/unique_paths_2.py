from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1-obstacleGrid[0][0]
        
        for i in range(1,m):
            if(obstacleGrid[i][0]!=1):dp[i][0] = dp[i-1][0]
            
        for j in range(1,n):
            if(obstacleGrid[0][j]!=1):dp[0][j] = dp[0][j-1]
        
        for i in range(1,m):
            for j in range(1,n):
                if(obstacleGrid[i][j]!=1):dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
        
# time complexity: O(mn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        m,n = list(map(int,input().strip().split()))
        grid = [list(map(int,input().strip().split())) for _ in range(m)]
        print(Solution().uniquePathsWithObstacles(grid))