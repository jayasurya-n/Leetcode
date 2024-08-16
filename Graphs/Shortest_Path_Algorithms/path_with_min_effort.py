from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n = len(heights), len(heights[0])
        effort = [[sys.maxsize]*n for _ in range(m)]
        
        effort[0][0] = 0
        pq = [(0,(0,0))]
        
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        
        while pq:
            eff,(i,j) = heapq.heappop(pq)
            if((i,j)==(m-1,n-1)):return eff
            
            for k in range(4):
                x = i+dx[k]
                y = j+dy[k]
                if(x<m and x>=0 and 
                   y<n and y>=0):
                    
                    neweff = max(eff, abs(heights[x][y]-heights[i][j]))
                    if(neweff<effort[x][y]):
                        effort[x][y] = neweff
                        heapq.heappush(pq,(neweff,(x,y)))


# time complexity: O(nmlogn(nm))
# space complexity: O(nm)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))