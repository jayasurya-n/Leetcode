from typing import List,Optional
import sys
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)]

        # dp[i][buy][cap] = max profit we can generate from day i to n-1, 
        # with and option to buy or sell the stock depending on value and having max cap as 0/1/2
        # buy = 0 means option to buy and no selling
        # buy = 1 means option to sell and no buing 

        for i in range(n-1,-1,-1):
            for buy in range(0,2):
                for cap in range(1,3):
                    if(buy==1):
                        dp[i][1][cap] = max(-prices[i]+dp[i+1][0][cap],dp[i+1][1][cap])
                    else:
                        dp[i][0][cap] = max(prices[i]+dp[i+1][1][cap-1],dp[i+1][0][cap])
        return dp[0][1][2]





# time complexity: O(6n)
# space complexity: O(6n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        prices = list(map(int,input().strip().split()))
        print(Solution().maxProfit(prices))