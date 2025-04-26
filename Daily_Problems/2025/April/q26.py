from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        ans = start = 0
        maxi = mini = -1 
        for i in range(n):
            if(minK>nums[i] or nums[i]>maxK):
                start = i+1
                maxi = mini = -1
                continue
            
            if(nums[i]==maxK):maxi = i
            if(nums[i]==minK):mini = i
            
            if(maxi!=-1 and nums[maxi]==maxK and 
               mini!=-1 and nums[mini]==minK):ans+=min(maxi,mini)-start+1
            
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))