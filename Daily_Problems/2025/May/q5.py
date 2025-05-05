from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def numTilings(self, n: int) -> int:
        # if(n<=1):return 1
        # elif(n==2):return 2
        
        # mod = 10**9 + 7
        # dp = [[0]*4 for _ in range(n+1)]
        # dp[0][3] = 1
        # dp[1][0] = dp[1][3] = 1
        # dp[2][0] = dp[2][1] = dp[2][2] = 1
        # dp[2][3] = 2
        
        # # dp[k][j]: ways to fill till tile k with j as the column state at kth tile 
        # # j = 0: empty 
        # # j = 1: top filled
        # # j = 1: bottom  filled
        # # j = 2: both  filled
        
        # for k in range(3,n+1):
        #     dp[k][0] = dp[k-1][3]
        #     dp[k][1] = (dp[k-1][2]+dp[k-2][3])%mod
        #     dp[k][2] = (dp[k-1][1]+dp[k-2][3])%mod
        #     dp[k][3] = (dp[k-1][3]+dp[k-1][1]+dp[k-1][2]+dp[k-2][3])%mod
        
        # return dp[n][3]

        
        
        
        # if(n<=1):return 1
        # elif(n==2):return 2
        
        # mod = 10**9 + 7
        # dp = [[0]*3 for _ in range(n+1)]
        # dp[0][0] = dp[1][0] = 1
        # dp[2][1] = dp[2][2] = 1
        # dp[2][0] = 2
        
        # # dp[k][j]: ways to fill till tile k with j as the column state at kth tile 
        # # j = 0: both filled
        # # j = 1: top filled
        # # j = 2: bottom  filled
        
        # for k in range(3,n+1):
        #     dp[k][1] = (dp[k-1][2]+dp[k-2][0])%mod
        #     dp[k][2] = (dp[k-1][1]+dp[k-2][0])%mod
        #     dp[k][0] = (dp[k-1][0]+dp[k-1][1]+dp[k-1][2]+dp[k-2][0])%mod
        # return dp[n][0]

        
        
        if(n<=1):return 1
        elif(n==2):return 2
        
        mod = 10**9 + 7
        dp = [[0]*2 for _ in range(n+1)]
        dp[0][0] = dp[1][0] = 1
        dp[2][1] = dp[2][0] = 2
        
        # dp[k][j]: ways to fill till tile k with j as the column state at kth tile 
        # j = 0: both filled
        # j = 1: only top/bottom filled
        
        for k in range(3,n+1):
            dp[k][1] = (dp[k-1][1]+2*dp[k-2][0])%mod
            dp[k][0] = (dp[k-1][0]+dp[k-1][1]+dp[k-2][0])%mod
        return dp[n][0]

# time complexity: O(n),O(n),O(n)
# space complexity: O(n),O(n),O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        print(Solution().numTilings(n))