from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        ans = cnt = 0
        i = 0
        for j in range(len(nums)):
            if(nums[j]==maxi):cnt+=1
            
            while(i<=j and cnt==k):
                ans+=len(nums)-j
                if(nums[i]==maxi):cnt-=1
                i+=1
        
        return ans    

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))