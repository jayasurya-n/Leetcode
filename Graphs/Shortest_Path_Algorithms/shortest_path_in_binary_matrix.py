from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]):
        n = len(grid)
        if(grid[0][0]!=0 or grid[n-1][n-1]!=0):return -1
        if(n==1 and grid[0][0]==0):return 1
        
        distance = [[sys.maxsize]*n for _ in range(n)]
        distance[0][0] = 0
        
        dx = [1,-1,0,0,1,1,-1,-1]
        dy = [0,0,1,-1,1,-1,1,-1]
        
        pq = [(1,(0,0))]
        
        while pq:
            d,(i,j) = heapq.heappop(pq)
            for k in range(8):
                x = i+dx[k]
                y = j+dy[k]
                if(x<n and x>=0 and 
                   y<n and y>=0 and grid[x][y]==0 and distance[x][y]>d+1):
                    distance[x][y] = d+1
                    heapq.heappush(pq,(d+1,(x,y)))
        
        if(distance[n-1][n-1]==sys.maxsize):return -1
        return distance[n-1][n-1]
        
# time complexity: O(n^2)
# space complexity: O(n^2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))