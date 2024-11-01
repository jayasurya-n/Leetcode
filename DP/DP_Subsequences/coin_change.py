from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        
        for i in range(1,amount+1):
            for coin in coins:
                if i>=coin:dp[i] = min(dp[i],dp[i-coin]+1)        
        return dp[amount] if dp[amount]!=(amount+1) else -1 

# time complexity: O(mn)
# space complexity: O(m)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        coins = list(map(int,input().strip().split()))
        amount = int(input().strip())
        print(Solution().coinChange(coins,amount))