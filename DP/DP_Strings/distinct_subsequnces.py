from typing import List,Optional
import sys
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1 = len(s)
        l2 = len(t)
        dp = [[0]*(l2+1) for _ in range(l1+1)]
        
        for i in range(l1+1):
            dp[i][0] = 1


        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if(s[i-1]!=t[j-1]):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]+dp[i-1][j-1]
        return dp[l1][l2]



# time complexity: O(l1*l2)
# space complexity: O(l1*l2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        t = input().strip()
        print(Solution().numDistinct(s,t))