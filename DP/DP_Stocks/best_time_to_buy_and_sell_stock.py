from typing import List,Optional
import sys
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        mini = prices[0]
        profit = 0
        ans = 0
        for i in range(1,n):
            profit = prices[i]-mini
            ans = max(ans,profit)
            mini = min(mini,prices[i])
        return ans


# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        prices = list(map(int,input().strip().split()))
        print(Solution().maxProfit(prices))