from typing import List,Optional
import sys
from sys import setrecursionlimit
setrecursionlimit(10**9)

class Solution:
    def minimumEnergy(self, height, n):
        dp = [-1]*(n)
        dp[0] = 0
        for i in range(1,n):
            dp[i] = abs(height[i]-height[i-1])+dp[i-1]
            if(i>=2):dp[i] = min(dp[i],abs(height[i]-height[i-2])+dp[i-2])
        return dp[n-1]

    # def findminEnergy(self,n,dp,height):
    #     if(n==0):return 0

    #     if(dp[n]!=-1):return dp[n]
    #     dp[n] = self.findminEnergy(n-1,dp,height)+abs(height[n]-height[n-1])
    #     if(n>=2):dp[n] = min(dp[n],self.findminEnergy(n-2,dp,height)+abs(height[n]-height[n-2]))
    #     return dp[n]
             
    # def minimumEnergy(self, height, n):
    #     dp = [-1]*(n)
    #     return self.findminEnergy(n-1,dp,height)


# time complexity: O(n),O(n)
# space complexity: O(n), O(n+n(stack space))
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        n = int(input().strip())
        height = list(map(int,input().strip().split()))
        print(Solution().minimumEnergy(height,n))
