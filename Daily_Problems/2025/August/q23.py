from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])

        def minimumArea(x1,x2,y1,y2) -> int:
            if(x1>x2 or y1>y2 or x1<0 or y1<0 or x2>=m or y2>=n):return 10**10
            xmin,xmax,ymin,ymax = m,-1,n,-1
            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    if(grid[i][j]==1):
                        xmin = min(xmin,i)
                        xmax = max(xmax,i)
                        ymin = min(ymin,j)
                        ymax = max(ymax,j)
            return (xmax-xmin+1)*(ymax-ymin+1) 

        ans = m*n
        for r in range(m):
            for c in range(n):
                ans = min(ans,minimumArea(0,r,0,n-1)+
                          minimumArea(r+1,m-1,0,c)+
                          minimumArea(r+1,m-1,c+1,n-1))
                
                ans = min(ans,minimumArea(0,r,0,c)+
                          minimumArea(r+1,m-1,0,c)+
                          minimumArea(0,m-1,c+1,n-1))
                
        for c in range(m):
            for r in range(n):
                ans = min(ans,minimumArea(0,m-1,0,c)+
                          minimumArea(0,r,c+1,n-1)+
                          minimumArea(r+1,m-1,c+1,n-1))
                
                ans = min(ans,minimumArea(0,r,0,c)+
                          minimumArea(0,r,c+1,n-1)+
                          minimumArea(r+1,m-1,0,n-1))

        for r1 in range(m):
            for r2 in range(r1+1,m):
                ans = min(ans,minimumArea(0,r1,0,n-1)+
                          minimumArea(r1+1,r2,0,n-1)+
                          minimumArea(r2+1,m-1,0,n-1))

        for c1 in range(n):
            for c2 in range(c1+1,n):
                ans = min(ans,minimumArea(0,m-1,0,c1)+
                          minimumArea(0,m-1,c1+1,c2)+
                          minimumArea(0,m-1,c2+1,n-1))
        
        return ans


# time complexity: O(mn(m+n)^2)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))