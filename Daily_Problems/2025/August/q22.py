from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        xmin,xmax,ymin,ymax = m,-1,n,-1
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    xmin = min(xmin,i)
                    xmax = max(xmax,i)
                    ymin = min(ymin,j)
                    ymax = max(ymax,j)

        return (xmax-xmin+1)*(ymax-ymin+1)

# time complexity: O(mn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))