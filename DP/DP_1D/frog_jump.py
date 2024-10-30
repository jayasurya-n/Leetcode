from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minimumEnergy(self, height, n):
        if(n<=1):return 0
        dp = [sys.maxsize]*(n+1)
        dp[1] = 0
        dp[2] = abs(height[1]-height[0])
         
        for i in range(3,n+1):
            dp[i] = min(dp[i],dp[i-1]+abs(height[i-1]-height[i-2]),
                        dp[i-2]+abs(height[i-1]-height[i-3]))
        return dp[n]
            
# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        height = list(map(int,input().strip().split()))
        print(Solution().minimumEnergy(height,n))
