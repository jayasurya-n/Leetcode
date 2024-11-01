from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def knapSack(self, n, W, profits, weights):
        dp = [[0]*(W+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            for w in range(W+1):
                dp[i][w] = dp[i-1][w]
                if(weights[i-1]<=w):
                    dp[i][w] = max(dp[i][w],dp[i][w-weights[i-1]]+profits[i-1])
        return dp[n][W]
        
# time complexity: O(nW)
# space complexity: O(nW)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        W = int(input().strip())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        print(Solution().knapSack(n,W,val,wt))