from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n=  len(nums)
        nums.sort()

        def check(x):
            cnt = 0
            i = 0
            while i<n-1:
                if(nums[i+1]-nums[i]<=x):
                    cnt+=1
                    i+=1
                i+=1
            return cnt>=p

        low,high = 0,nums[n-1]-nums[0]
        while(low<=high):
            mid = (low+high)>>1
            if(check(mid)):high = mid-1
            else:low = mid+1
        return low

# time complexity: O(nlogn+nlogK)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))