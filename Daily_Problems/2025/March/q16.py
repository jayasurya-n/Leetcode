from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(t):
            cnt = 0
            for rank in ranks:
                cnt+=int(math.sqrt(t/rank))
            return cnt>=cars
        
        low = 1
        high = max(ranks)*cars*cars
        while(low<=high):
            mid = (low+high)>>1
            if(check(mid)):high = mid-1
            else:low = mid+1
        return low
        
# time complexity: O(nlog(max(n)))
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))