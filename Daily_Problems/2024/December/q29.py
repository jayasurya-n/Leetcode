from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def numWays(self, words: List[str], target: str) -> int:        
        n,m = len(target),len(words[0])
        mod = 10**9+7
        freq = [[0]*26 for _ in range(m)]
        
        for word in words:
            for j,ch in enumerate(word):
                freq[j][ord(ch)-ord('a')]+=1
        
        # dp[i][j]: no of ways to form first i characters from first j columns of words
        dp = [[0]*(m+1) for _ in range(n+1)]
        for j in range(m+1):dp[0][j] = 1
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                dp[i][j]=dp[i][j-1]
                dp[i][j]+=freq[j-1][ord(target[i-1])-ord('a')]*dp[i-1][j-1]
                dp[i][j]%=mod
        return dp[n][m]

# time complexity: O(nm+mL)
# space complexity: O(nm+mL)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))