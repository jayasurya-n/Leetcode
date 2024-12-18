from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def eggDrop(self,n, k):
        dp = [[k+2]*n  for _ in range(k+1)]
        for j in range(n):
            dp[0][j] = 0
            dp[1][j] = 1
        for i in range(k+1):dp[i][0] = i
        
        for i in range(2,k+1):
            for j in range(1,n):
                for f in range(1,i+1):
                    dp[i][j] = min(dp[i][j],1+max(dp[f-1][j-1],dp[i-f][j]))
        return dp[k][n-1]

# time complexity: O(nk^2)
# space complexity: O(nk)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))