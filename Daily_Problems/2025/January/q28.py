from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        visited = [[False]*n for _ in range(m)]
        
        def dfs(i,j):
            visited[i][j] = True
            cnt = grid[i][j]
            for di,dj in [(0,1),(0,-1),(-1,0),(1,0)]:
                ni,nj = i+di,j+dj
                if(0<=ni<m and 0<=nj<n and grid[ni][nj]>0 and not visited[ni][nj]):cnt+=dfs(ni,nj)
            return cnt
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if(not visited[i][j] and grid[i][j]>0):ans=max(ans,dfs(i,j))
        return ans    

# time complexity: O(mn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))