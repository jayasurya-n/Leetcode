from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0]*(high+1)
        dp[0] = 1
        mod = 10**9+7
        
        for l in range(1,high+1):
            if(l>=zero):dp[l]=(dp[l-zero]+dp[l])%mod
            if(l>=one):dp[l]=(dp[l-one]+dp[l])%mod
        
        ans = 0
        for i in range(low,high+1):ans=(ans+dp[i])%mod
        return ans

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))