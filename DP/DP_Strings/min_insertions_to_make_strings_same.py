from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1,n2 = len(word1),len(word2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if(word1[i-1]==word2[j-1]):dp[i][j]=dp[i-1][j-1]+1
                else:dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        
        return n1+n2-2*dp[n1][n2]
    
# time complexity: O(mn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        word1 = input().strip()
        word2 = input().strip()
        print(Solution().minDistance(word1,word2))