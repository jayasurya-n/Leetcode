from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # grid = [['S']*n for _ in range(m)]
        # for i,j in walls:
        #     grid[i][j] = 'W'
        
        # for i,j in guards:
        #     grid[i][j] = 'G'
        
        # for r,c in guards:
        #     for i in range(r+1,m):
        #         if(grid[i][c]=='W' or grid[i][c]=='G'):break
        #         grid[i][c] = 'NS'
            
        #     for i in range(r-1,-1,-1):
        #         if(grid[i][c]=='W' or grid[i][c]=='G'):break
        #         grid[i][c] = 'NS'
            
        #     for j in range(c+1,n):
        #         if(grid[r][j]=='W' or grid[r][j]=='G'):break
        #         grid[r][j] = 'NS' 

        #     for j in range(c-1,-1,-1):
        #         if(grid[r][j]=='W' or grid[r][j]=='G'):break
        #         grid[r][j] = 'NS'

        # return sum([sum(1 if ele=='S' else 0 for row in grid for ele in row)])
    

        grid = [['S']*n for _ in range(m)]
        for i,j in walls:
            grid[i][j] = 'W'
        
        for i,j in guards:
            grid[i][j] = 'G'
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i,j,dir):
            if(i<0 or j<0 or i>=m or j>=n or 
               grid[i][j]=='W' or grid[i][j]=='G'):return

            grid[i][j] = 'NS'
            dfs(i+directions[dir][0],j+directions[dir][1],dir)


        for dir in range(4):
            for i,j in guards:
                dfs(i+directions[dir][0],j+directions[dir][1],dir)

        return sum([sum(1 if ele=='S' else 0 for row in grid for ele in row)])

# time complexity: O(mn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))