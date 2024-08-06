from typing import List,Optional
import sys
class Solution:
    def knapSack(self, n, W, val, wt):
        dp = [[0]*(W+1) for _ in range(n)]

        for w in range(0,W+1):
            dp[0][w] = val[0]*(w//wt[0])

        for i in range(1,n):
            for w in range(0,W+1):
                dp[i][w] = dp[i-1][w]
                if(wt[i]<=w):
                    dp[i][w] = max(dp[i][w], dp[i][w-wt[i]]+val[i])
        return dp[n-1][W]
                


# time complexity: O(W*n)
# space complexity: O(W*n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        W = int(input().strip())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        print(Solution().knapSack(n,W,val,wt))