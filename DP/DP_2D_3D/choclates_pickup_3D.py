from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def solve(self, m, n, grid):
        dp = [[[0]*n for _ in range(n)] for _ in range(m)]
        
        for j1 in range(n):
            for j2 in range(n):
                dp[m-1][j1][j2] = grid[m-1][j1]+(grid[m-1][j2] if j1!=j2 else 0)
        
        for i in range(m-2,-1,-1):
            for j1 in range(n):
                for j2 in range(n):
                    for k1 in [-1,0,1]:
                        for k2 in [-1,0,1]:
                            nj1 = j1+k1
                            nj2 = j2+k2
                            if(0<=nj1<n and 0<=nj2<n):
                                dp[i][j1][j2] = max(dp[i][j1][j2],
                                            dp[i+1][nj1][nj2]+grid[i][j1]+(grid[i][j2] if j1!=j2 else 0))
        return dp[0][0][n-1]
                        
# time complexity: O(mn^2)
# space complexity: O(mn^2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,m = list(map(int,input().strip().split()))
        grid = [list(map(int,input().strip().split())) for _ in range(n)]
        print(Solution().solve(n,m,grid))