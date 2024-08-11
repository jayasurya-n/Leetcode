from typing import List,Optional
from collections import deque
import sys
class Solution:
    def orangesRotting(self, grid: List[List[int]]) :
        m = len(grid)
        n = len(grid[0])
        
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        def bfs(start):
            q = deque()            
            for pair in start:q.append(pair)
            
            while(q):
                print(q)
                size = len(q)
                for _ in range(size):
                    i,j,t = q.popleft()
                    self.time = max(self.time,t)
                    for k in range(4):
                        x = i+dx[k]
                        y = j+dy[k]
                        if(x<m and x>=0 and y<n and y>=0 and grid[x][y]==1):
                            grid[x][y] = 2
                            q.append((x,y,t+1))
       
        self.time = 0
        start = []
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==2):start.append((i,j,0))
        
        bfs(start)
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):return -1
        return self.time
            
            
# time complexity: O(m*n)
# space complexity: O(m*n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        m,n = list(map(int,input().strip().split()))
        grid = [list(map(int,input().strip().split())) for _ in range(m)]
        print(Solution().orangesRotting(grid))