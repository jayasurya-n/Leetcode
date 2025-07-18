from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//3
        max_heap = [-nums[i] for i in range(n)]
        tsum = -sum(max_heap)
        heapq.heapify(max_heap)

        dp_min= [0]*(n+1)
        dp_min[0] = tsum
        for i in range(n,2*n):
            heapq.heappush(max_heap,-nums[i])
            dp_min[i-n+1] = dp_min[i-n]+nums[i]+heapq.heappop(max_heap)
            

        min_heap = [nums[i] for i in range(2*n,3*n)]
        tsum = sum(min_heap)
        heapq.heapify(min_heap)

        ans = dp_min[n]-tsum
        for i in range(2*n-1,n-1,-1):
            heapq.heappush(min_heap,nums[i])
            tsum+=nums[i]-heapq.heappop(min_heap)
            ans = min(ans,dp_min[i-n]-tsum)
        
        return ans

# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))