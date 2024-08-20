from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def stoneGameII(self, piles: List[int]):
        n = len(piles)
        dp = [[-1]*(n+1) for _ in range(n)]
        suffixSum = [0]*n
        suffixSum[-1] = piles[-1]
        for i in range(n-2,-1,-1):
            suffixSum[i] = suffixSum[i+1]+piles[i]
        
        def solve(i,m):
            if(i>=n):return 0
            if(dp[i][m]!=-1):return dp[i][m]
            
            ans = 0 
            sum = 0
            for x in range(1,2*m+1):
                ans = max(ans,suffixSum[i]-solve(i+x,max(x,m)))
                    
            dp[i][m] = ans
            return ans
            
        return solve(0,1)


# time complexity: O(n^3)
# space complexity: O(n^2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))