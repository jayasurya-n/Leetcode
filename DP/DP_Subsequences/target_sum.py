from typing import List,Optional
import sys
class Solution:
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     n = len(nums)
    #     total = sum(nums)
    #     dp = dict()
    #     if(nums[0]!=0):
    #         dp[(0,nums[0])] = 1 
    #         dp[(0,-nums[0])] = 1
    #     else:dp[(0,0)]=2
    #     for ind in range(1,n):
    #         for t in range(-total,total+1):
    #             dp[(ind,t)] = dp.get((ind-1,t-nums[ind]),0)+dp.get((ind-1,t+nums[ind]),0) 
    #     print(dp)
    #     return dp.get((n-1,target),0)

    def findTargetSumWays(self, arr: List[int], d: int) -> int:
        n = len(arr)
        totalSum = sum(arr)
        if((totalSum+d)%2==1):return 0
        if(d>totalSum):return 0
        target = (totalSum-d)//2


        dp = [[0]*(target+1) for _ in range(n)]

        for i in range(n):dp[i][0] = 1
        if(arr[0]<=target):
            if(arr[0]==0):dp[0][arr[0]]=2
            else:dp[0][arr[0]] = 1

        for i in range(1,n):
            for s in range(0,target+1):
                dp[i][s] = dp[i-1][s]
                if(arr[i]<=s):
                    dp[i][s] = (dp[i-1][s] + dp[i-1][s-arr[i]])

        return dp[n-1][target]


# time complexity: O(sum*n), O(n*sum)
# space complexity: O(sum*n), O(n*sum)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        nums = list(map(int,input().strip().split()))
        target = int(input().strip())
        print(Solution().findTargetSumWays(nums,target))