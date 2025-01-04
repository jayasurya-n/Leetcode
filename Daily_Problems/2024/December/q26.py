from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        tsum = sum(nums)
        dp = [[0]*(2*tsum+1) for _ in range(n)]
        if(abs(target)>tsum):return 0
        
        dp[0][tsum+nums[0]]=1
        dp[0][tsum-nums[0]]+=1
        
        for i in range(1,n):
            for s in range(0,2*tsum+1):
                if(0<=s-nums[i]<2*tsum+1):dp[i][s]+=dp[i-1][s-nums[i]]
                if(0<=s+nums[i]<2*tsum+1):dp[i][s]+=dp[i-1][s+nums[i]]
        return dp[n-1][target+tsum]
    
# time complexity: O(n*sum)
# space complexity: O(n*sum)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))