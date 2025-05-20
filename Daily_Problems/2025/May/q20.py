from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        dec = [0]*(n+1)
        for l,r in queries:
            dec[l]+=1
            dec[r+1]-=1
        
        for i in range(1,n+1):
            dec[i]+=dec[i-1]
        
        for i in range(n):
            if(dec[i]<nums[i]):
                return False
        return True

# time complexity: O(m+n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))