from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # the code similar to trapping rain water I wont work here
        # because each cell is not only dependent on its row and column
        # but also depends on many cells as the water cannot flow higher than boundaries. 
        m,n = len(heightMap),len(heightMap[0])
        pq = []
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            pq.append((heightMap[i][0],i,0))
            pq.append((heightMap[i][n-1],i,n-1))
            visited[i][0] = True
            visited[i][n-1] = True
        
        for j in range(1,n-1):
            pq.append((heightMap[0][j],0,j))
            pq.append((heightMap[m-1][j],m-1,j))
            visited[0][j] = True
            visited[m-1][j] = True
        
        heapq.heapify(pq)
        ans = 0
        while pq:
            h,x,y = heapq.heappop(pq)
            for dx,dy in [(0,1),(0,-1),(-1,0),(1,0)]:
                nx,ny = x+dx,y+dy
                if(0<=nx<m and 0<=ny<n and not visited[nx][ny]):
                    nh = heightMap[nx][ny]
                    visited[nx][ny] = True
                    ans+=max(0,h-nh)
                    heapq.heappush(pq,(max(nh,h),nx,ny))
        return ans

# time complexity: O(mnlognmn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))