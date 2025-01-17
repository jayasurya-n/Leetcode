from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def isPossible(mid):
            stores = 0
            for size in quantities:
                stores+=(size+mid-1)//mid
            return stores<=n
        
        low,high = 1,max(quantities)
        while(low<=high):
            mid = (low+high)//2
            if(isPossible(mid)):high = mid-1
            else:low = mid+1
        return low
                
# time complexity: O(mlog(max(m)))
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))