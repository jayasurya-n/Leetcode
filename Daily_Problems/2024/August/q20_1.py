from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    # def stoneGame(self, piles: List[int]):
    #     n = len(piles)
    #     dp = [[-1]*n for _ in range(n)]
        
    #     def solve(i,j):
    #         if(i>j):return 0
    #         if(dp[i][j]!=-1):return dp[i][j]
            
    #         parity = (j-i)%2
    #         if(parity==1):dp[i][j] = max(piles[i]+solve(i+1,j), piles[j]+solve(i,j-1))
    #         else:dp[i][j] = max(-piles[i]+solve(i+1,j), -piles[j]+solve(i,j-1))
    #         return dp[i][j]
        
    #     return solve(0,n-1)>0

    def stoneGame(self, piles: List[int]):
        n = len(piles)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = piles[i]
            
        for l in range(2,n+1):
            for i in range(0,n+1-l):
                j = i+l-1
                dp[i][j] = max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1])
        
        return dp[0][n-1]>0
                
            
    def stoneGame(self, piles: List[int]):
        return True


# time complexity: O(n^2),O(n^2),O(1)
# space complexity: O(n^2),O(n^2),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))