from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1,n2 = len(s),len(t)
        # dp[i][j]: number of distinct subsequnces of s[0:i] that can form t[0:j] 
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        for i in range(n1+1):dp[i][0] = 1 
        
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if(s[i-1]==t[j-1]):
                    # consider this letter as matching or dont 
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
                else:dp[i][j] = dp[i-1][j]
        
        return dp[n1][n2]
                
# time complexity: O(mn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        t = input().strip()
        print(Solution().numDistinct(s,t))