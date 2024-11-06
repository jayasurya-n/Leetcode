from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*n
        
        for i in range(n):
            maxi = 0
            for j in range(1,min(i+1,k)+1):
                maxi = max(maxi,arr[i-j+1])
                if(i>=j):dp[i] = max(dp[i],dp[i-j]+j*maxi)
                else:dp[i] = max(dp[i],j*maxi)
        return dp[n-1]

# time complexity: O(n*k)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))