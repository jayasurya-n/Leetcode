from typing import List,Optional
import sys
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0]*(l2+1) for _ in range(l1+1)]

        for j in range(0,l2):dp[0][j] = 0
        for i in range(0,l1):dp[i][0] = 0
        
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if(word1[i-1]==word2[j-1]):
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        return l1+l2 - 2*dp[l1][l2]


# time complexity: O(l1*l2)
# space complexity: O(l1*l2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        word1 = input().strip()
        word2 = input().strip()
        print(Solution().minDistance(word1,word2))