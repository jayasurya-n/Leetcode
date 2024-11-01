from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        totalSum = sum(nums)
        if(target<-totalSum or target>totalSum):return 0
        offset = totalSum
        dp = [[0]*(2*totalSum+1) for _ in range(n+1)]
        dp[0][offset]=1
        
        for i in range(1,n+1):
            for s in range(-totalSum,totalSum+1):
                if(s+nums[i-1]<=totalSum):dp[i][s+offset]+=dp[i-1][s+nums[i-1]+offset]
                if(s-nums[i-1]>=-totalSum):dp[i][s+offset]+=dp[i-1][s-nums[i-1]+offset]
        return dp[n][target+offset]

# time complexity: O(n*sum)
# space complexity: O(n*sum)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        nums = list(map(int,input().strip().split()))
        target = int(input().strip())
        print(Solution().findTargetSumWays(nums,target))