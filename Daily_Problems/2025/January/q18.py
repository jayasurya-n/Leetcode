from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        costs = [[sys.maxsize]*n for _ in range(m)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        values = {1:(0,1),2:(0,-1),3:(1,0),4:(-1,0)}
        
        pq = [(0,(0,0))]
        costs[0][0] = 0
        
        while pq:
            cost,(x,y) = heapq.heappop(pq)
            if((x,y)==(m-1,n-1)):return cost
            
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if(0<=nx<m and 0<=ny<n):
                    ncost = cost
                    if((dx,dy)!=values[grid[x][y]]):ncost+=1
                    if(costs[nx][ny]>ncost):
                        heapq.heappush(pq,(ncost,(nx,ny)))
                        costs[nx][ny] = ncost
                    

# time complexity: O((v+e)logv), e = mn, v = mn
# space complexity: O(v+e)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))