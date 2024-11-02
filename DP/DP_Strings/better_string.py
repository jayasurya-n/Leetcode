from typing import List,Optional
import sys
class Solution:
    def countSubsets(self,s):
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        # last = [-1]*26
        # for i in range(1,n+1):
        #     dp[i] = 2*dp[i-1]
        #     if(last[ord(s[i-1]) - ord('a')]!=-1):
        #         dp[i]-=dp[last[ord(s[i-1])-ord('a')]-1]
        #     last[ord(s[i-1])-ord('a')] = i
        # return dp[n]

        last = {}
        for i in range(1,n+1):
            dp[i] = 2*dp[i-1]
            if(s[i-1] in last):
                dp[i]-=dp[last[s[i-1]]-1]
            last[s[i-1]] = i
        return dp[n]

    def betterString(self, str1, str2):
        c1 = self.countSubsets(str1)
        c2 = self.countSubsets(str2)
        return str1 if c1>=c2 else str2

# time complexity: O(n+m)
# space complexity: O(n+m)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        str1 = input().strip()
        str2 = input().strip()
        print(Solution().betterString(str1,str2))