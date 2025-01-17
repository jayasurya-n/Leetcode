from typing import List,Optional
from collections import deque
import sys,math
class Solution:
    def minDays(self, grid: List[List[int]]):
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i,j,visited):
            dx = [-1,0,1,0]
            dy = [0,1,0,-1]
            visited[i][j] = True
            
            for k in range(4):
                x = i+dx[k]
                y = j+dy[k]
                if(x<m and x>=0 and
                   y<n and y>=0 and 
                   not visited[x][y] and grid[x][y]==1):dfs(x,y,visited)
            
        
        def countIslands():
            visited = [[0]*n for _ in range(m)]
            cnt = 0
            for i in range(m):
                for j in range(n):
                    if(not visited[i][j] and grid[i][j]==1):
                        cnt+=1
                        dfs(i,j,visited)
            
            return cnt

        if(countIslands()!=1):return 0
        

        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    grid[i][j]=0
                    if(countIslands()!=1):return 1
                    grid[i][j]=1
        
        return 2
                    

# time complexity: O((m^2*n^2))
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))