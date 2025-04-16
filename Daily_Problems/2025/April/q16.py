from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hash = defaultdict(int)
        pairs = ans = 0
        
        i = j = 0
        while j<n:
            hash[nums[j]]+=1
            pairs+=hash[nums[j]]-1
            while i<j and pairs>=k:
                hash[nums[i]]-=1
                pairs-=hash[nums[i]]
                ans+=(n-j)
                i+=1
            j+=1
        
        return ans

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        nums = lii()
        k = ii()
        print(Solution().countGood(nums,k))