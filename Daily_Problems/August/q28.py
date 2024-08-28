from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]):
        m,n = len(grid1),len(grid1[0])
        
        def dfs(i,j):
            visited[i][j] = True
            dx = [1,-1,0,0]
            dy = [0,0,1,-1]
            
            bool = True
            for k in range(4):
                x = i+dx[k]
                y = j+dy[k]
                if(x>=0 and x<m and 
                   y>=0 and y<n and 
                   not visited[x][y] and  
                   grid2[x][y]==1):
                    if(grid1[x][y]==0):bool = False
                    bool &= dfs(x,y)

            return bool
        
        ans = 0
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if(not visited[i][j] and grid2[i][j]==1 and grid1[i][j]==1):
                    print("i,j:",i,j)
                    if(dfs(i,j)):
                        ans+=1
        
        return ans


# time complexity: O(mn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        m,n = list(map(int,input().strip().split()))
        grid1 = [list(map(int,input().strip().split())) for _ in range(m)]
        grid2 = [list(map(int,input().strip().split())) for _ in range(m)]
        print(Solution().countSubIslands(grid1,grid2))