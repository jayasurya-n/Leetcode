from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def cutRod(self, price, n):
        dp = [0]*(n+1)
        for i in range(1,n+1):
            for l in range(1,i+1):
                dp[i] = max(dp[i],dp[i-l]+price[l-1])
        return dp[n]

# time complexity: O(n^2)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        price = list(map(int,input().strip().split()))
        print(Solution().cutRod(price,n))