from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def rec(i,xor):
            if(i==len(nums)):return xor
            return rec(i+1,xor^nums[i])+rec(i+1,xor)
        
        return rec(0,0)

# time complexity: O(2^n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))