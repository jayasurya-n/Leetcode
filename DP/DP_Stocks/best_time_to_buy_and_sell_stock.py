from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n = len(prices)
        # maxi = prices[-1]
        # ans = 0 
        # for i in range(n-2,-1,-1):
        #     ans = max(ans,maxi-prices[i])
        #     maxi = max(maxi,prices[i])
        # return ans
        
        n = len(prices)
        mini = prices[0]
        ans = 0
        for i in range(1,n):
            ans = max(ans,prices[i]-mini)
            mini = min(mini,prices[i])
        return ans
        
# time complexity: O(n),O(n)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))