from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def climbStairs(self, n: int) -> int:
        if(n<=2):return n
        dp = [0]*(n+1)
        dp[1] = 1;dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))