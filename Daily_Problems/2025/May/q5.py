from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def numTilings(self, n: int) -> int:
        if(n<=1):return 1
        elif(n==2):return 2
        
        mod = 10**9 + 7
        dp = [0]*(n+1)
        # dp[k]: no of ways to fill 2*k board
        # transition: dp[k] = dp[k-1]+dp[k-2]+g[n-1]+f[n-1]
        
        # g[n] = f[n-1]+dp[n-2]
        # f[n] = g[n-1]+dp[n-2]
        # f[n] = g[n] = sigma(dp[n-2])
    
        # dp[k] = 2*dp[k-1]+dp[k-3]
        # base: dp[0],dp[1],dp[2] = 1,1,2
        # final: dp[n]
        
        dp[0],dp[1],dp[2] = 1,1,2
        for k in range(3,n+1):
            dp[k] = (2*dp[k-1]+dp[k-3])%mod
        return dp[n]

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))