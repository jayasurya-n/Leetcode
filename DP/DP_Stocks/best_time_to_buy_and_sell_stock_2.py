from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n+1)]

        # dp[i][buy] = max profit we can generate from day i to n-1, 
        # with and option to buy or sell the stock depending on value
        # buy = 1 means can buy but no selling
        # buy = 0 means can sell but no buying 

        for i in range(n-1,-1,-1):
            for buy in [0,1]:
                if(buy==1):
                    dp[i][1] = max(-prices[i]+dp[i+1][0],dp[i+1][1])
                else:
                    dp[i][0] = max(prices[i]+dp[i+1][1],dp[i+1][0])
        for row in dp:print(row)
        return dp[0][1]

        # # Greedy(Just summing up all the positives)
        # ans = 0
        # start = prices[0]
        # for i in range(1,len(prices)):
        #     if(start<prices[i]):
        #         ans+=prices[i]-start
        #     start=prices[i]
        # return ans

# time complexity: O(2n),O(n)
# space complexity: O(2n),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        prices = list(map(int,input().strip().split()))
        print(Solution().maxProfit(prices))