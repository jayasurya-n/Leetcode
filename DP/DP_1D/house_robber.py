from typing import List,Optional
import sys
class Solution:
    # def maxMoney(self,n,dp,nums):
    #     if(n<0):return 0
    #     if(dp[n]!=-1):return dp[n]
    #     dp[n] = max(self.maxMoney(n-2,dp,nums)+nums[n],
    #                     self.maxMoney(n-1,dp,nums))
    #     return dp[n]

    # def rob(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [-1]*n
    #     return max(self.maxMoney(n-1,dp,nums),self.maxMoney(n-2,dp,nums))

    # def rob(self, nums: List[int]) -> int:
    #         n = len(nums)
    #         if(n==1):return nums[0]
    #         dp = [-1]*n
    #         dp[0],dp[1] = nums[0],nums[1]
    #         for i in range(2,n):
    #             dp[i] = max(nums[i]+dp[i-2],dp[i-1])
    #         return dp[n-1]

    def rob(self, nums: List[int]) -> int:
            n = len(nums)
            if(n==1):return nums[0]
            lastPrev,prev = nums[0],max(nums[0],nums[1])
            ans = prev
            for i in range(2,n):
                ans = max(nums[i]+lastPrev,prev)
                lastPrev = prev
                prev = ans
            return ans


# time complexity: O(n),O(n),O(n)
# space complexity: O(n+n(stack space)),O(n),O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        nums = list(map(int,input().strip().split()))
        print(Solution().rob(nums))