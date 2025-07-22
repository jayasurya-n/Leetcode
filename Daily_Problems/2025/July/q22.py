from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = curr = 0
        hash = set()
        i = 0
        for j in range(len(nums)):            
            while i<j and nums[j] in hash:
                curr-=nums[i]
                hash.remove(nums[i])
                i+=1

            curr+=nums[j]
            hash.add(nums[j])
            ans = max(ans,curr)
        
        return ans

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))