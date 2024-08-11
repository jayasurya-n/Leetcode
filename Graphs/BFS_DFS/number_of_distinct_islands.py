from typing import List,Optional
from collections import deque
import sys
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]):
        m,n = len(grid),len(grid[0])
        
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        def bfs(si,sj):
            q = deque([(si,sj)])
            visited[si][sj] = True
            island = []
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
                            island.append((x-si,y-sj))
            islands.add(tuple(island))

        islands = set()
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1 and not visited[i][j]):bfs(i,j)
                     
        return len(islands)

# time complexity: O(5mn)
# space complexity: O(2mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        m,n = list(map(int,input().strip().split()))
        grid = [list(map(int,input().strip().split())) for _ in range(m)]
        print(Solution().countDistinctIslands(grid))