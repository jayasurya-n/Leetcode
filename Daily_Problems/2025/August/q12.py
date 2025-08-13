from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9+7
        k = 1
        for i in range(1,n+1):
            if(pow(i,x,mod)<=n):k = i
            else:break
        
        # dp[i][val]: ways to form val such that biggest number used is i
        dp = [[0]*(n+1) for _ in range(k+1)]
        for i in range(k+1):dp[i][0] = 1

        for i in range(1,k+1):
            temp = pow(i,x,mod)
            for val in range(1,n+1):
                dp[i][val] = dp[i-1][val]
                if(temp<=val):
                    dp[i][val]+=dp[i-1][val-temp]
                    dp[i][val]%=mod
        
        return dp[k][n]

# time complexity: O(n*k)
# space complexity: O(n*k)
if __name__ == "__main__":
    for _ in range(ii()):
        n,x = lii()
        print(Solution().numberOfWays(n,x))