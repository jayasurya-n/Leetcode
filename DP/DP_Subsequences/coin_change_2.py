from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin,amount+1):dp[i]+=dp[i-coin]
        return dp[amount]

# time complexity: O(mn)
# space complexity: O(m)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        coins = list(map(int,input().strip().split()))
        amount = int(input().strip())
        print(Solution().coinChange(coins,amount))