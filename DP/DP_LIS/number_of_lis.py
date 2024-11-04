from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        count = [1]*n
        for i in range(1,n):
            for j in range(i):
                if(nums[j]<nums[i]):
                    if(dp[i]<1+dp[j]):
                        dp[i] = 1+dp[j]
                        count[i] = count[j]
                    elif(dp[i]==1+dp[j]):
                        count[i]+=count[j]
        
        maxLen = max(dp)
        return sum(count[i] for i in range(len(dp)) if dp[i]==maxLen)
        
# time complexity: O(n^2)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))