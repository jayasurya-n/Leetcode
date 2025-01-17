from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if(grid[0][1]>1 and grid[1][0]>1):return -1
        
        m,n = len(grid),len(grid[0])
        pq = [(0,0,0)]
        visited = [[False]*n for _ in range(m)]
        
        while pq:
            time,i,j = heapq.heappop(pq)
            if(i==m-1 and j==n-1):return time
            
            if(visited[i][j]):continue
            visited[i][j] = True
            
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                x = i+dx
                y = j+dy
                if(0<=x<m and 0<=y<n and not visited[x][y]):
                    flag = 1 if(grid[x][y]-time)%2==0 else 0
                    ntime = max(grid[x][y]+flag,time+1)
                    heapq.heappush(pq,(ntime,x,y))
        
# time complexity: O(mnlogmn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))