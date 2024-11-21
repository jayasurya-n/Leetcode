from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[-1]*n for _ in range(m)]
        
        for i,j in guards:grid[i][j]='G'
        for i,j in walls:grid[i][j]='W'
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i,j,dir):
            if(i<0 or i>=m or j<0 or j>=n or grid[i][j]=='W' or grid[i][j]=='G'):return
            grid[i][j] = 1
            dfs(i+directions[dir][0],j+directions[dir][1],dir)
        
        for dir in range(4):
            for i,j in guards:dfs(i+directions[dir][0],j+directions[dir][1],dir)

        ans = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==-1):ans+=1
        return ans
        
# time complexity: O(mn+g(m+n))
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        m,n = list(map(int,input().strip().split()))
        p,q = list(map(int,input().strip().split()))
        guards = [list(map(int,input().strip().split())) for _ in range(p)]
        walls = [list(map(int,input().strip().split())) for _ in range(q)]
        print(Solution().countUnguarded(m,n,guards,walls))