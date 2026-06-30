from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        k = r-l+1
        MOD = 10**9+7
        # dp = [[[0]*k for _ in range(n)] for _ in range(2)]

        # dp[0][i][x]: number of zizag arrays ending with x(decreasing) and length i+1, 
        # dp[1][i][x]: number of zizag arrays ending with x(increasing) and lenght i+1

        # converting it to dp[0][j]
        # converting it to dp[1][j]
        dp = [[0]*k for _ in range(2)]
        IprefixSum = [0]*(k+1)
        DprefixSum = [0]*(k+1)
        for x in range(k):
            dp[0][x] = dp[1][x] = 1
            IprefixSum[x+1] = IprefixSum[x]+1
            DprefixSum[x+1] = DprefixSum[x]+1

        for i in range(1,n):
            for x in range(k):
                dp[0][x] = (IprefixSum[k]-IprefixSum[x+1])%MOD
                dp[1][x] = DprefixSum[x]%MOD
            
            for x in range(k):
                IprefixSum[x+1]=(dp[1][x]+IprefixSum[x])%MOD
                DprefixSum[x+1]=(dp[0][x]+DprefixSum[x])%MOD
        
        return (IprefixSum[k]+DprefixSum[k])%MOD

# time complexity: O(n*k)
# space complexity: O(k)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))