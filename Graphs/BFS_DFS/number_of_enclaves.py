from typing import List,Optional
from collections import deque
import sys
class Solution:
    def numEnclaves(self, grid: List[List[int]]):
        m,n = len(grid),len(grid[0])
        
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        def bfs(start):
            q = deque(start)
            for i,j in start:visited[i][j] = True
            
            while q:
                size = len(q)
                for _ in range(size):
                    i,j = q.popleft()
                    for k in range(4):
                        x = i+dx[k]
                        y = j+dy[k]
                        if(x<m and x>=0 and 
                            y<n and y>=0 and 
                            not visited[x][y] and grid[x][y]==1):
                            visited[x][y] = True
                            q.append((x,y))
            
        visited = [[False]*n for _ in range(m)]
        start = []
        for i in range(m):
            if(grid[i][0]==1 and not visited[i][0]):start.append((i,0)) 
            if(grid[i][-1]==1 and not visited[i][-1]):start.append((i,n-1))
        
        for j in range(n):
            if(grid[0][j]==1 and not visited[0][j]):start.append((0,j))
            if(grid[-1][j]==1 and not visited[-1][j]):start.append((m-1,j))
        
        bfs(start)
        ans = 0            
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1 and not visited[i][j]):ans+=1
        return ans
    
# time complexity: O(4mn+m+n)
# space complexity: O(2mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))