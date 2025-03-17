from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)
        def check(x):
            if(x==0):return True
            cnt = 0
            for i in range(n):cnt+=candies[i]//x
            return cnt>=k
        
        low,high = 0,max(candies)
        while(low<=high):
            mid = (low+high)>>1
            if(check(mid)):low = mid+1
            else:high = mid-1
        return high

# time complexity: O(nlog(max(m)))
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))