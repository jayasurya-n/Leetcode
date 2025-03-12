from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def bsIndex(nums,target):
            # works like bisect.left
            # if target is lesser than smallest then index=0
            # if target is larger than largest  then index=n
            low,high = 0,len(nums)-1
            while(low<=high):
                mid = (low+high)>>1
                if(nums[mid]>=target):high = mid-1
                else:low = mid+1
            return low
        
        return max(len(nums)-bsIndex(nums,0.1),bsIndex(nums,0))

# time complexity: O(logn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))