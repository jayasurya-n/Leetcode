from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[0]*(n) for _ in range(m)]
        
        dx = [-1,0,1]
        for j in range(n-2,-1,-1):
            for i in range(m-1,-1,-1):
                for k in range(3):
                    ni,nj = i+dx[k],j+1
                    if(ni>=0 and ni<m and 
                       grid[i][j]<grid[ni][nj]):
                        dp[i][j] = max(dp[i][j],1+dp[ni][nj])
        
        ans = 0
        for i in range(m):ans=max(ans,dp[i][0])
        return ans
                
# time complexity: O(mn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))