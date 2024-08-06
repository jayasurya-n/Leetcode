from typing import List,Optional
import sys
class Solution:
    def minInsertions(self, s: str) -> int:
        l = len(s)
        rev = s[::-1]
        dp = [[0]*(l+1) for _ in range(l+1)]

        for j in range(0,l):dp[0][j] = 0
        for i in range(0,l):dp[i][0] = 0
        
        for i in range(1,l+1):
            for j in range(1,l+1):
                if(s[i-1]==rev[j-1]):
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return l - dp[l][l]


# time complexity: O(n*n)
# space complexity: O(n*n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        print(Solution().minInsertions(s))