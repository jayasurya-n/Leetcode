from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1,n):
            for j in range(i):
                if(nums[j]<nums[i]):
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
    
# time complexity: O(n^2)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))