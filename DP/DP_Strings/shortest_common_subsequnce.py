from typing import List,Optional
import sys
class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        dp = [[0]*(l2+1) for _ in range(l1+1)]

        for j in range(0,l2):dp[0][j] = 0
        for i in range(0,l1):dp[i][0] = 0
        
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if(str1[i-1]==str2[j-1]):
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        

        i,j=l1,l2
        ans = ""
        while(i>0 and j>0):
            if(str1[i-1]==str2[j-1]):
                ans = str1[i-1]+ans
                i-=1
                j-=1

            else:
                if(dp[i-1][j]>=dp[i][j-1]):
                    ans = str1[i-1]+ans
                    i-=1
                else:
                    ans = str2[j-1]+ans
                    j-=1
        while(i>0):
            ans = str1[i-1]+ans
            i-=1
        while(j>0):
            ans = str2[j-1]+ans
            j-=1
        return ans



# time complexity: O(l1*l2)
# space complexity: O(l1*l2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        str1 = input().strip()
        str2 = input().strip()
        print(Solution().shortestCommonSupersequence(str1,str2))