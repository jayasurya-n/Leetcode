from typing import List,Optional
import sys
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l1 = len(s)
        l2 = len(p)

        dp = [[False]*(l2+1) for _ in range(l1+1)]
        dp[0][0] = True
    
        for j in range(2,l2+1):
            if(p[j-1]=='*' and dp[0][j-2]==True):
                dp[0][j] = True

        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if(s[i-1]==p[j-1] or p[j-1]=='.'):
                    dp[i][j] = dp[i-1][j-1]
                elif(p[j-1]=='*'):
                    dp[i][j] = dp[i][j-2] #null case
                    if(p[j-2]=='.' or p[j-2]==s[i-1]):
                        dp[i][j] = dp[i-1][j] or dp[i][j]
                else:
                    dp[i][j] = False

        return dp[l1][l2]


# time complexity: O(l1*l2)
# space complexity: O(l1*l2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        p = input().strip()
        print(Solution().isMatch(s,p))