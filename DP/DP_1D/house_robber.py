from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n==1):return nums[0]
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i],dp[i-2]+nums[i],dp[i-1])
        return dp[n-1]

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        nums = list(map(int,input().strip().split()))
        print(Solution().rob(nums))