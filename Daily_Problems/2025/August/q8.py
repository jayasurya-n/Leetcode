from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def soupServings(self, n: int) -> float:
        # m = math.ceil(n/25)
        # if m>200:return 1.0

        # dp = [[0.0]*(m+1) for _ in range(m+1)]
        # dp[0][0] = 0.5
        # for i in range(1,m+1):
        #     dp[0][i] = 1.0
        #     dp[i][0] = 0.0

        # for i in range(1,m+1):
        #     for j in range(1,m+1):
        #         dp[i][j] = (
        #             dp[max(i-4, 0)][j] +
        #             dp[max(i-3, 0)][max(j-1, 0)] +
        #             dp[max(i-2, 0)][max(j-2, 0)] +
        #             dp[max(i-1, 0)][max(j-3, 0)])/4.0

        #     if dp[i][i] > 1-1e-5:return 1.0
        
        # return dp[m][m]

        m = math.ceil(n/25)

        def solve(i,j):
            if(i<=0 and j<=0):return 0.5
            if(i<=0 and j>0):return 1.0
            if(i>0 and j<=0):return 0.0

            if((i,j) in dp):return dp[(i,j)]
            dp[(i,j)] = (
                solve(i-4,j) +
                solve(i-3,j-1) +
                solve(i-2,j-2) +
                solve(i-1,j-3))/4.0
            return dp[(i,j)]

        dp = defaultdict(float)
        for i in range(1,m+1):
            if(solve(i,i)>1-1e-5):return 1.0
        
        return dp[(m,m)]

# time complexity: O(m^2),O(m^2)
# space complexity: O(m^2),O(m^2)
if __name__ == "__main__":
    for _ in range(1):
        for n in range(0,200):
            print(Solution().soupServings(n*25))