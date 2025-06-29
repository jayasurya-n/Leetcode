from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mod = 10**9+7
        nums.sort()
        ans = 0
        for i in range(n):
            if(2*nums[i]<=target):ans = (ans+1)%mod
            ind = bisect.bisect_right(nums,target-nums[i],0,i)
            ans+=(pow(2,ind,mod)-1)*(pow(2,i-ind,mod))
            ans%=mod
        return ans

        # n = len(nums)
        # mod = 10**9+7
        # nums.sort()
        # ans = 0
        # i,j = 0,n-1

        # while i<=j:
        #     if(nums[i]+nums[j]<=target):
        #         ans+=pow(2,j-i,mod)
        #         ans%=mod
        #         i+=1
        #     else:j-=1
        # return ans

# time complexity: O(nlogn),O(nlogn)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        nums = lii()
        print(Solution().func(nums,n))