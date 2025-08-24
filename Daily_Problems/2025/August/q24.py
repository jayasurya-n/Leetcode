from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        suffix = [0]*(n+2)
        cnt = 0
        for i in range(n-1,-1,-1):
            if(nums[i]==1):cnt+=1
            else:cnt = 0
            suffix[i+1] = cnt
        
        ans = cnt = 0
        for i in range(n):
            ans = max(ans,suffix[i+2]+cnt)
            if(nums[i]==1):cnt+=1
            else:cnt = 0

        return ans

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))