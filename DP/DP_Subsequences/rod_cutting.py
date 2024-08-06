from typing import List,Optional
import sys
class Solution:
    def cutRod(self, price, n):
        dp = [[0]*(n+1) for _ in range(n)]

        for j in range(1,n+1):
            dp[0][j] = price[0]*j

        for i in range(1,n):
            for rodlen in range(0,n+1):
                dp[i][rodlen] = dp[i-1][rodlen]
                if(i+1<=rodlen):
                    dp[i][rodlen] = max(dp[i][rodlen],dp[i][rodlen-(i+1)]+price[i])
        return dp[n-1][n] 

                

# time complexity: O(n^2)
# space complexity: O(n^2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        price = list(map(int,input().strip().split()))
        print(Solution().cutRod(price,n))