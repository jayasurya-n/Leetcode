from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        hash = set()
        for num in nums:hash.add(num)
        d = len(hash)
        
        i = j = 0
        ans = 0
        hash = defaultdict(int)
        while j<n:
            hash[nums[j]]+=1
            while(i<=j and len(hash)==d):
                ans+=n-j
                hash[nums[i]]-=1
                if(hash[nums[i]]==0):hash.pop(nums[i])
                i+=1    
            j+=1
        return ans

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))