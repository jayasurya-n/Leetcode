from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    # def maxWidthRamp(self, nums: List[int]) -> int:
    #     pairs = [(nums[i],i) for i in range(len(nums))]
    #     pairs.sort()
        
    #     min_index = len(nums)
    #     ans = 0
    #     for _,index in pairs:
    #         min_index = min(min_index,index)
    #         ans = max(ans,index-min_index)
    #     return ans

    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i in range(len(nums)):
            if(not stack or nums[stack[-1]]>nums[i]):stack.append(i)
        
        ans = 0
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[i]:
                ind = stack.pop()
                ans = max(ans,i-ind)
        return ans
                
# time complexity: O(nlogn),O(n)
# space complexity: O(n),O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))