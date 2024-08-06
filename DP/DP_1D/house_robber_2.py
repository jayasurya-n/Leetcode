from typing import List,Optional
import sys
class Solution:
    def maxMoney(self,n,nums):
            n = len(nums)
            if(n==1):return nums[0]
            lastPrev,prev = nums[0],max(nums[0],nums[1])
            ans = prev
            for i in range(2,n):
                ans = max(nums[i]+lastPrev,prev)
                lastPrev = prev
                prev = ans
            return prev


    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n==1):return nums[0]
        return max(self.maxMoney(n-1,nums[1:]),self.maxMoney(n-1,nums[:-1]))
    


# time complexity: O(n)
# space complexity: O(n+n)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        nums = list(map(int,input().strip().split()))
        print(Solution().rob(nums))