from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if(sum(nums)%2):return False
        
        # dp[csum] : tells if csum is possbile   
        # transition: dp[csum]+=dp[csum-nums[i]]
        # final: dp[target]
        target = sum(nums)//2
        dp = [0]*(target+1)
        dp[0] = 1
        
        for i in range(n):
            for csum in range(target,nums[i]-1,-1):
                dp[csum]|=dp[csum-nums[i]]
        return True if dp[target] else False 

# time complexity: O(n*sum)
# space complexity: O(sum)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))