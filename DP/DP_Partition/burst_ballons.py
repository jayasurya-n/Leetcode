from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        # dp[i][i+1] = 0
        
        for l in range(2,n):
            for i in range(0,n-l):
                j = i+l
                # we are choosing k as the last baloon to burst in range(i,j)
                # this allows to divide into independent sub problems
                for k in range(i+1,j):
                    cost = nums[i]*nums[k]*nums[j]+dp[i][k]+dp[k][j]
                    dp[i][j] = max(dp[i][j],cost)
        return dp[0][n-1]

# time complexity: O(n^3)
# space complexity: O(n^2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))