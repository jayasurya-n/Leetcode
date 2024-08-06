from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        n = int(input().strip())
        weights = list(map(int,input().strip().split()))
        values = list(map(int,input().strip().split()))
        W = int(input().strip())

        dp = [[0]*(W+1) for _ in range(n)]
        for w in range(weights[0],W+1):
            dp[0][w] = values[0]

        for i in range(1,n):
            for w in range(0,W+1):
                dp[i][w] = dp[i-1][w]
                if(weights[i]<=w):
                    dp[i][w] = max(dp[i][w], dp[i-1][w-weights[i]]+values[i])
        return dp[n-1][W]
                


# time complexity: O(W*n)
# space complexity: O(W*n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())