from typing import List,Optional
from collections import deque
import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,grid):
        m = len(grid)
        n = len(grid[0])
        
        visited = [[False]*n for _ in range(m)]
        dx = [-1,1,0,0,-1,1,-1,1]
        dy = [0,0,-1,1,-1,1,1,-1]
        
        def dfs(i,j):
            visited[i][j] = True
            for k in range(8):
                x = i+dx[k]
                y = j+dy[k]
                if(x<m and x>=0 and y<n and y>=0 and 
                   grid[x][y]==1 and 
                   not visited[x][y]):dfs(x,y)

        islands = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1 and not visited[i][j]):
                    dfs(i,j)
                    islands+=1
        return islands

# time complexity: O(mn)
# space complexity: O(mn+m+n(stack space))
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        m,n = list(map(int,input().strip().split()))
        grid = [list(map(int,input().strip().split())) for _ in range(m)]
        print(Solution().numIslands(grid))