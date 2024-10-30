from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):dp[i][0] = 1
        for j in range(n):dp[0][j] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
        
# time complexity: O(mn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        m,n = list(map(int,input().strip().split()))
        print(Solution().uniquePaths(m,n))