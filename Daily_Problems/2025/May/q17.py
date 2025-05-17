from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = nums.count(0)
        ones = nums.count(1)
        
        for i in range(len(nums)):
            if(i<zero):nums[i] = 0
            elif(zero<=i<zero+ones):nums[i] = 1
            else:nums[i] = 2 

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))