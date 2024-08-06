from typing import List,Optional
import sys
class Solution:
    def longestCommonSubstr(self, s1, s2, m, n):
        # code here
        dp = [[0]*(n+1) for _ in range(m+1)]
        ans = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(s1[i-1]==s2[j-1]):
                    dp[i][j] = dp[i-1][j-1]+1
                    ans = max(ans,dp[i][j])
        return ans



# time complexity: O(m*n)
# space complexity: O(m*n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s1 = input().strip()
        s2 = input().strip()
        print(Solution().longestCommonSubstr(s1,s2,len(s1),len(s2)))