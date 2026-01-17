from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        hmax = hcur = 1
        for i in range(1,len(hBars)):
            if(hBars[i]==hBars[i-1]+1):hcur+=1
            else:hcur = 1
            hmax = max(hmax,hcur)

        vmax = vcur = 1
        for i in range(1,len(vBars)):
            if(vBars[i]==vBars[i-1]+1):vcur+=1
            else:vcur = 1
            vmax = max(vmax,vcur)
        
        max_side = min(hmax,vmax)+1
        return max_side*max_side


# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))