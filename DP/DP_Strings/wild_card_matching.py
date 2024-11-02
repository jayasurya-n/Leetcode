from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1,n2 = len(p),len(s)
        # dp[i][j]: returns whether pattern p[0:i] can match string s[0:j]
        dp = [[False]*(n2+1) for _ in range(n1+1)]
        dp[0][0] = True
        
        for i in range(1,n1+1):
            if(p[i-1]=='*'):dp[i][0] = dp[i-1][0]
        
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if(p[i-1]==s[j-1] or p[i-1]=='?'):dp[i][j] = dp[i-1][j-1]
                elif(p[i-1]=='*'):dp[i][j] = dp[i][j-1] or dp[i-1][j]      
        return dp[n1][n2]
                
# time complexity: O(mn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        p = input().strip()
        print(Solution().isMatch(s,p))