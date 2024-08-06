from typing import List,Optional
import sys
from sys import setrecursionlimit
setrecursionlimit(10**9)

class Solution:
    # def findminCost(self,n,k,dp,height):
    #     if(n==0):return 0
        
    #     if(dp[n]!=-1):return dp[n]
    #     cost = sys.maxsize
    #     minimum = sys.maxsize
    #     for i in range(1,k+1):
    #         if(i<=n):cost = self.findminCost(n-i,k,dp,height)+abs(height[n]-height[n-i])
    #         minimum = min(minimum,cost)
    #     dp[n] = minimum
    #     return minimum

    # def minimizeCost(self, height, n, k):
    #     dp = [-1]*n
    #     return self.findminCost(n-1,k,dp,height)

    def minimizeCost(self, height, n, k):
        dp = [sys.maxsize]*(n)
        dp[0] = 0
        for i in range(1,n):
            for j in range(1,k+1):
                if(j<=i):
                    dp[i] = min(dp[i],dp[i-j]+abs(height[i]-height[i-j]))
        return dp[n-1]
        
# time complexity: O(n*k),O(n*k)
# space complexity: O(n+n(stack space)), O(n)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        n,k = list(map(int,input().strip().split()))
        height = list(map(int,input().strip().split()))
        print(Solution().minimizeCost(height,n,k))
