from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        less = curr = 0

        freq = [0]*(2*n+1)
        freq[n] = 1

        for i in range(n):
            if(nums[i]==target):
                less+=freq[curr+n]
                curr+=1
            else:
                curr-=1
                less-=freq[curr+n]
            
            freq[curr+n]+=1
            ans+=less
        return ans

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))