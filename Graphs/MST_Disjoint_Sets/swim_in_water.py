from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]):
        m,n = len(grid),len(grid[0])
        pq = [(grid[0][0],0,0)]
        visited = [[False]*n for _ in range(m)]
        visited[0][0] = True
        
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
         
        ans = 0
        while pq:
            t,i,j = heapq.heappop(pq)
            ans = max(ans, t)
            if(i==m-1 and j==n-1):return ans
            for k in range(4):
                x = i+dx[k]
                y = j+dy[k]
                if(x<m and x>=0 and 
                    y<n and y>=0 and not visited[x][y]):
                    visited[x][y] = True
                    heapq.heappush(pq,(grid[x][y],x,y))
        
        return -1
        

# time complexity: O(n^2logn)
# space complexity: O(n^2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))