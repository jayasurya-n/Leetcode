from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    mod = 10**9+7
    def topDown(self, n):
        def fib(n,dp):
            if(n<=1):return n
            if(dp[n]!=-1):return dp[n]
            dp[n] = (fib(n-1,dp)+fib(n-2,dp))%self.mod
            return dp[n]
        
        dp = [-1]*(n+1)
        return fib(n,dp)
        
    def bottomUp(self, n):
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = (dp[i-1]+dp[i-2])%self.mod
        return dp[n]

# time complexity: O(n), O(n)
# space complexity: O(n+n(stack space)), O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        print(Solution().topDown(n))   
        print(Solution().bottomUp(n))