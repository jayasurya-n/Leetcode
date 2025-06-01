from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(limit,n)+1):
            if(n-i>2*limit):continue
            ans+= min(n-i,limit)-max(n-i-limit,0)+1
        return ans
        
        
        def nc2(n):
            if(n<0 or n<2):return 0
            return (n*(n-1))//2
        
        ans = nc2(n+2)
        ans-= 3*nc2(n+2-(limit+1))
        ans+= 3*nc2(n+2-2*(limit+1))
        ans-= nc2(n+2-3*(limit+1))
        return ans
        
# time complexity: O(min(n,limit)),O(1)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))