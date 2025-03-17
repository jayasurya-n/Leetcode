from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def check(x):
            cnt = 0
            i = 0
            while i<n:
                if(nums[i]<=x):
                    cnt+=1
                    i+=2
                else:i+=1
            return cnt>=k 
        
        low,high = min(nums),max(nums)
        while(low<=high):
            mid = (low+high)>>1
            if(check(mid)):high = mid-1
            else:low = mid+1
        return low

# time complexity: O(nlog(max(m)))
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))