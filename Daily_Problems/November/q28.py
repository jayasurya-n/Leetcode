from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        distance = [[float('inf')]*n for _ in range(m)]
        distance[0][0] = grid[0][0]
        pq = [(distance[0][0],0,0)]
        
        while pq:
            d,x,y = heapq.heappop(pq)
            if(x==m-1 and y==n-1):return d
            
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny = x+dx,y+dy
                if(0<=nx<m and 0<=ny<n):
                    newd = grid[nx][ny]+d
                    if(distance[nx][ny]>newd):
                        distance[nx][ny] = newd
                        heapq.heappush(pq,(newd,nx,ny))
                
# time complexity: O(mnlogmn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        m,n = list(map(int,input().strip().split()))
        grid = [list(map(int,input().strip().split())) for _ in range(m)]
        print(Solution().minimumObstacles(grid))