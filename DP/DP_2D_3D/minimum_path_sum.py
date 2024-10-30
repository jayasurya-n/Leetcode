from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for i in range(1,m):dp[i][0]=dp[i-1][0]+grid[i][0]
        for j in range(1,n):dp[0][j]=dp[0][j-1]+grid[0][j]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[m-1][n-1]
        
# time complexity: O(mn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        m,n = list(map(int,input().strip().split()))
        grid = [list(map(int,input().strip().split())) for _ in range(m)]
        print(Solution().minPathSum(grid))