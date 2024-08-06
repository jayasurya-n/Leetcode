from typing import List,Optional
import sys
class Solution:
    def solve(self,n,dp):
        if(n<=1):return 1

        if(dp[n]!=-1):return dp[n]
        dp[n] = self.solve(n-1,dp)+self.solve(n-2,dp)
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        return self.solve(n,dp)
        pass




# time complexity: O(n)
# space complexity: O(n+n(stack space))
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        n = int(input().strip())
        print(Solution().climbStairs(n))