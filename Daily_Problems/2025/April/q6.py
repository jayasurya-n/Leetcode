from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # nums.sort()
        
        # # dp[i] largest subset ending at index i
        # # transition: for j in range(i):if (arr[i]%arr[j]==0 and len(dp[i])<len(dp[j])+1):
        # # dp[i] = dp[j].append(nums[i])
        # # final: dp[i] with maximum len(dp[i])
        # # base: dp[i] = [arr[i]]
        
        # dp = [[] for _ in range(n)]
        # for i in range(n):dp[i].append(nums[i])
        
        # for i in range(1,n):
        #     for j in range(i):
        #         if(nums[i]%nums[j]==0 and len(dp[i])<len(dp[j])+1):
        #             dp[i] = dp[j][::-1].append(nums[j]) 
        
        # ans = []
        # maxi = 0
        # for i in range(n):
        #     if(len(dp[i])>maxi):
        #         maxi = len(dp[i])
        #         ans = dp[i]
        # return ans
        
        
        
        n = len(nums)
        nums.sort()
        
        # dp[i] largest subset ending at index i
        # transition: for j in range(i):if (arr[i]%arr[j]==0 and dp[i]<dp[j]+1):
        # dp[i] = dp[j]+1
        # prev[i] = j
        # final: max(dp)
        # base: dp[i] = 1
        
        dp = [1]*n
        prev = [-1]*n
        
        for i in range(1,n):
            for j in range(i):
                if(nums[i]%nums[j]==0 and dp[i]<dp[j]+1):
                    dp[i] = dp[j]+1
                    prev[i] = j 
        
        i = dp.index(max(dp))
        ans = []
        while i!=-1:
            ans.append(nums[i])
            i = prev[i]
        return ans
        
# time complexity: O(n^2),O(n^2)
# space complexity: O(n^2),O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))