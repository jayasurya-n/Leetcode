from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):dp[i][i]=1
        
        for l in range(2,n+1):
            for i in range(n-l+1):
                j = i+l-1
                if(s[i]==s[j]):dp[i][j] = dp[i+1][j-1]+2
                else:dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][n-1]
    
# time complexity: O(n^2)
# space complexity: O(n^2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        print(Solution().longestPalindromeSubseq(s))