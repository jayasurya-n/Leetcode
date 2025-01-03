from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # n = len(nums)
        # psum = [0]*n
        # for i in range(n):
        #     psum[i] = (psum[i-1] if i>0 else 0) + nums[i]
        
        # ans = 0
        # for i in range(n-1):
        #     if(2*psum[i]>=psum[-1]):ans+=1
        # return ans
        
        n = len(nums)
        l,r = 0,sum(nums)
        ans = 0
        for i in range(n-1):
            l+=nums[i]
            r-=nums[i]
            if(l>=r):ans+=1
        return ans

# time complexity: O(n),O(n)
# space complexity: O(n),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))