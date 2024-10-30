from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        dp = [0]*(n)
        for i in range(1,n):
            ans = sys.maxsize
            for jump in range(1,k+1):
                if(jump<=i):ans = min(ans,dp[i-jump]+abs(arr[i]-arr[i-jump]))
            dp[i] = ans
        return dp[n-1]
        
# time complexity: O(nk)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,k = list(map(int,input().strip().split()))
        height = list(map(int,input().strip().split()))
        print(Solution().minimizeCost(height,n,k))
