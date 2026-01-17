from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)

        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                (ix1,iy1),(ix2,iy2) = bottomLeft[i],topRight[i]
                (jx1,jy1),(jx2,jy2) = bottomLeft[j],topRight[j]
                
                xlen = min(ix2,jx2)-max(ix1,jx1)
                if(xlen<0):xlen=0

                ylen = min(iy2,jy2)-max(iy1,jy1)
                if(ylen<0):ylen=0

                ans = max(ans,min(xlen,ylen))
        return ans*ans

# time complexity: O(n^2)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))