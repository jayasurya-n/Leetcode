from typing import List,Optional
import sys
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        dp = [[0]*(l2+1) for _ in range(l1+1)]

        for j in range(0,l2):dp[0][j] = 0
        for i in range(0,l1):dp[i][0] = 0
        
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if(text1[i-1]==text2[j-1]):
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[l1][l2]



# time complexity: O(l1*l2)
# space complexity: O(l1*l2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        text1 = input().strip()
        text2 = input().strip()
        print(Solution().longestCommonSubsequence(text1,text2))