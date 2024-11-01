from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        n = int(input().strip())
        weights = list(map(int,input().strip().split()))
        values = list(map(int,input().strip().split()))
        W = int(input().strip())

        dp = [[0]*(W+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for w in range(W+1):
                dp[i][w] = dp[i-1][w]
                if(weights[i-1]<=w):
                    dp[i][w] = max(dp[i][w],dp[i-1][w-weights[i-1]]+values[i-1])
        return dp[n][W]
        
# time complexity: O(nW)
# space complexity: O(nW)
                


# time complexity: O(W*n)
# space complexity: O(W*n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())