from typing import List,Optional
import sys

from sys import setrecursionlimit
setrecursionlimit(10**5)

class Solution:
    mod = 1000000000+7
    def fibTopDown(self,n,dp):
        if(n<=1):return n

        if(dp[n]!=-1):return dp[n]
        dp[n] = ((self.fibTopDown(n-1,dp)%self.mod)+(self.fibTopDown(n-2,dp)%self.mod))%(self.mod)
        return dp[n] 

    def topDown(self, n):
        dp = [-1]*(n+1)
        return self.fibTopDown(n,dp)

    def bottomUp(self, n):
        dp = [-1]*(n+1)
        dp[1] = 1;dp[0] = 0
        for i in range(2,n+1):
            dp[i] = (dp[i-1]+dp[i-2])%self.mod
        return dp[n]




# time complexity: O(n), O(n)
# space complexity: O(n+n(stack space)), O(n)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        n = int(input().strip())
        print(Solution().topDown(n))   
        print(Solution().bottomUp(n))   