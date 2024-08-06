from typing import List,Optional
import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n)]
        for i in range(n):dp[i][0] = 0
        for i in range(0,amount+1):
            if(i%coins[0]==0):
                dp[0][i] = i//coins[0]
            else:dp[0][i] = 10**9
        
        for ind in range(1,n):
            for amou in range(0,amount+1):
                dp[ind][amou] = dp[ind-1][amou]
                if(coins[ind]<=amou):
                    dp[ind][amou] = min(dp[ind][amou],dp[ind][amou-coins[ind]]+1)

        if(dp[n-1][amount]>=10**9):return -1
        return dp[n-1][amount]
        
        
# time complexity: O(n*amount)
# space complexity: O(n*amount)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        coins = list(map(int,input().strip().split()))
        amount = int(input().strip())
        print(Solution().coinChange(coins,amount))