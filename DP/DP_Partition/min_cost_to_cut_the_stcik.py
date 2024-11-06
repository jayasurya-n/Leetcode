from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0]+cuts+[n]
        m = len(cuts)
        dp = [[sys.maxsize]*m for _ in range(m)]
        for i in range(m-1):dp[i][i+1] = 0
        
        for l in range(2,m):
            for i in range(0,m-l):
                j = i+l
                for k in range(i+1,j):
                    cost = cuts[j]-cuts[i]+dp[i][k]+dp[k][j]
                    dp[i][j] = min(dp[i][j],cost)
        return dp[0][m-1]
                
# time complexity: O(m^3)
# space complexity: O(m^2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))